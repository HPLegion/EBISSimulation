"""
This module contains the basic simulation method.
"""
from __future__ import annotations
from typing import Optional, Dict, Any, Union
import numpy as np
import scipy.integrate
import scipy.interpolate

from .. import xs
from ..elements import Element
from ..physconst import Q_E
from ._result import BasicResult
from._basic_helpers import BasicDevice


def basic_simulation(element: Union[Element, str, int], j: float, e_kin: float, t_max: float,
                     dr_fwhm: Optional[float] = None, N_initial: Optional[np.ndarray] = None,
                     CNI: bool = False,
                     solver_kwargs: Optional[Dict[str, Any]] = None) -> BasicResult:
    """
    Interface for performing basic charge breeding simulations.

    These simulations only include the most important effects, i.e. electron ionisation,
    radiative recombination and optionally dielectronic recombination (for those transitions whose
    data is available in the resource directory). All other effects are ignored.

    Continuous Neutral Injection (CNI) can be activated on demand.

    The results only represent the proportions of different charge states, not actual densities.

    Parameters
    ----------
    element :
        An instance of the Element class, or an identifier for the element, i.e. either its
        name, symbol or proton number.
    j :
        <A/cm^2>
        Current density
    e_kin :
        <eV>
        Electron beam energy
    t_max :
        <s>
        Simulated breeding time
    dr_fwhm :
        <eV>
        If a value is given, determines the energy spread of the electron beam
        (in terms of Full Width Half Max) and hence the effective width of DR resonances.
        Otherwise DR is excluded from the simulation.
    N_initial :
        Determines the initial charge state distribution if given, must have Z + 1 entries, where
        the array index corresponds to the charge state.
        If no value is given the distribution defaults to 100% of 1+ ions at t = 0 s, or a small
        amount of neutral atoms in the case of CNI.
    CNI :
        If Continuous Neutral Injection is activated, the neutrals are assumed to form an
        infinite reservoir. Their absolute number will not change over time and hence they act as a
        constant source of new singly charged ions. Therefore the absolute amount of ions increases
        over time.
    solver_kwargs :
        If supplied these keyword arguments are unpacked in the solver call.
        Refer to the documentation of scipy.integrate.solve_ivp for more information.

    Returns
    -------
        An instance of the BasicResult class, holding the simulation parameters, timesteps and
        charge state distribution.
    """
    # cast element to Element if necessary
    element = Element.as_element(element)

    # set initial conditions if not supplied by user
    if N_initial is None:
        N_initial = np.zeros(element.z + 1)
        if CNI:
            N_initial[0] = 1
        else:
            N_initial[1] = 1

    # prepare solver options
    if not solver_kwargs:
        solver_kwargs = {}
    solver_kwargs.setdefault("method", "LSODA")

    # convert current density A/cm**2 to particle flux density electrons/s/m**2
    j_human = j
    j = j * 1.e4 / Q_E

    # compute cross section
    xs_mat = xs.eixs_mat(element, e_kin) + xs.rrxs_mat(element, e_kin)
    if dr_fwhm:
        xs_mat += xs.drxs_mat(element, e_kin, dr_fwhm)
    if CNI:
        xs_mat[0] = 0

    # the jacobian of a basic simulation
    _jac = j * xs_mat
    if solver_kwargs["method"] == "LSODA":
        jac = lambda _, N: _jac  # LSODA solver requires "callable" jacobian  # noqa:E731
    else:
        jac = _jac

    dNdt = lambda _, N: _jac.dot(N)  # noqa:E731

    res = scipy.integrate.solve_ivp(dNdt, (0, t_max), N_initial, jac=jac, **solver_kwargs)
    return BasicResult(t=res.t, N=res.y, res=res,
                       device=BasicDevice(e_kin=e_kin, j=j_human, fwhm=dr_fwhm), target=element)
