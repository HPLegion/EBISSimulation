"""
Module containing the classes providing access to the relevant cross section for ionisation and
recombination
"""

# from functools import lru_cache
import math
import numpy as np
import numba

from .physconst import RY_EV, ALPHA, PI, COMPT_E_RED

# XS_CACHE_MAXSIZE = 1024 # The max number of cached cross section results per function

@numba.njit
def _normpdf(x, mu, sigma):
    """
    The pdf of the normal distribution f_mu,sigma(x).


    Parameters
    ----------
    x : numpy.ndarray
        Function argument
    mu : numpy.ndarray
        Mean of the distribution
    sigma : numpy.ndarray
        Standard deviation of the distribution

    Returns
    -------
    out : numpy.ndarray
        Value of the normal PDF evaluated elementwise on the input arrays
    """
    return np.exp(-(x - mu)**2 / (2 * sigma**2)) / (2 * PI * sigma**2)**0.5


@numba.njit
def eixs_vec(element, e_kin):
    """
    Electron ionisation cross section according to a simplified version of the models given in [1]_.

    Parameters
    ----------
    element : ebisim.Element
        An ebisim.Element object that holds the required physical information for cross section
        calculations.
    e_kin : float
        <Unit: eV>
        Kinetic energy of the impacting electron.

    Returns
    -------
    out : numpy.ndarray
        <Unit m^2>
        The cross sections for each individual charge state, where the array-index corresponds
        to the charge state, i.e. out[q] ~ cross section of q+ ion.

    References
    ----------
    .. [1] "An empirical formula for the electron-impact ionization cross-section",
           W. Lotz,
           Zeitschrift Für Physik, 206(2), 205–211 (1967),
           https://doi.org/10.1007/BF01325928

    See Also
    --------
    ebisim.eixs_mat : Similar method with different output format.

    """
    css = element.e_bind.shape[0]
    shells = element.e_bind.shape[1]
    xs_vec = np.zeros(css + 1)
    for cs in range(css):
        xs = 0
        for shell in range(shells):
            e = element.e_bind[cs, shell]
            n = element.cfg[cs, shell]
            if e_kin > e and n > 0:
                xs += n * math.log(e_kin / e) / (e_kin * e)
        xs_vec[cs] = xs
    xs_vec *= 4.5e-18
    return xs_vec

@numba.njit
def eixs_mat(element, e_kin):
    """
    Electron ionisation cross section according to a simplified version of the models given in [1]_.

    Parameters
    ----------
    element : ebisim.Element
        An ebisim.Element object that holds the required physical information for cross section
        calculations.
    e_kin : float
        <Unit: eV>
        Kinetic energy of the impacting electron.

    Returns
    -------
    out : numpy.array
        <Unit m^2>
        The cross sections for each individual charge state, arranged in a matrix suitable
        for implementation of a rate equation like dN/dt = j * xs_matrix dot N.
        out[q, q]   = - cross section of q+ ion
        out[q+1, q] = + cross section of (q+1)+ ion

    References
    ----------
    .. [1] "An empirical formula for the electron-impact ionization cross-section",
           W. Lotz,
           Zeitschrift Für Physik, 206(2), 205–211 (1967),
           https://doi.org/10.1007/BF01325928

    See Also
    --------
    ebisim.eixs_vec : Similar method with different output format.

    """
    xs = eixs_vec(element, e_kin)
    return np.diag(xs[:-1], -1) - np.diag(xs)


@numba.njit
def rrxs_vec(element, e_kin):
    """
    Radiative recombination cross section according to [1]_.

    Parameters
    ----------
    element : ebisim.Element
        An ebisim.Element object that holds the required physical information for cross section
        calculations.
    e_kin : float
        <Unit: eV>
        Kinetic energy of the impacting electron.

    Returns
    -------
    out : numpy.ndarray
        <Unit m^2>
        The cross sections for each individual charge state, where the array-index corresponds
        to the charge state, i.e. out[q] ~ cross section of q+ ion.

    References
    ----------
    .. [1] "Direct radiative recombination of electrons with atomic ions:
           Cross sections and rate coefficients",
           Young Soon Kim and R. H. Pratt,
           Phys. Rev. A 27, 2913 (1983),
           https://journals.aps.org/pra/abstract/10.1103/PhysRevA.27.2913

    See Also
    --------
    ebisim.rrxs_mat : Similar method with different output format.

    """
    chi = 2 * element.z_eff**2 * RY_EV / e_kin
    xs = 8 * PI * ALPHA / (3 * np.sqrt(3)) * COMPT_E_RED**2 * \
            chi * np.log(1 + chi/(2 * element.n_0_eff**2))
    xs[0] = 0
    return xs


@numba.njit
def rrxs_mat(element, e_kin):
    """
    Radiative recombination cross section according to [1]_.

    Parameters
    ----------
    element : ebisim.Element
        An ebisim.Element object that holds the required physical information for cross section
        calculations.
    e_kin : float
        <Unit: eV>
        Kinetic energy of the impacting electron.

    Returns
    -------
    out : numpy.array
        <Unit m^2>
        The cross sections for each individual charge state, arranged in a matrix suitable
        for implementation of a rate equation like dN/dt = j * xs_matrix dot N.
        out[q, q]   = - cross section of q+ ion
        out[q, q+1] = + cross section of (q+1)+ ion

    References
    ----------
    .. [1] "Direct radiative recombination of electrons with atomic ions:
           Cross sections and rate coefficients",
           Young Soon Kim and R. H. Pratt,
           Phys. Rev. A 27, 2913 (1983),
           https://journals.aps.org/pra/abstract/10.1103/PhysRevA.27.2913

    See Also
    --------
    ebisim.rrxs_vec : Similar method with different output format.

    """
    xs = rrxs_vec(element, e_kin)
    return np.diag(xs[1:], 1) - np.diag(xs)


@numba.njit
def drxs_vec(element, e_kin, fwhm):
    """
    Dielectronic recombination cross section.
    The cross sections are estimated by weighing the strength of each transition with the
    profile of a normal Gaussian distribution. This simulates the effective spreading of the
    resonance peaks due to the energy spread of the electron beam

    Parameters
    ----------
    element : ebisim.Element
        An ebisim.Element object that holds the required physical information for cross section
        calculations.
    e_kin : float
        <Unit: eV>
        Kinetic energy of the impacting electron.
    fwhm : float
        <Unit: eV>
        Energy spread to apply for the resonance smearing, expressed in terms of
        full width at half maximum.

    Returns
    -------
    out : numpy.ndarray
        <Unit m^2>
        The cross sections for each individual charge state, where the array-index corresponds
        to the charge state, i.e. out[q] ~ cross section of q+ ion.


    See Also
    --------
    ebisim.drxs_mat : Similar method with different output format.

    """
    xs_vec = np.zeros(element.z + 1)
    if element.dr_cs.size > 0:
        sig = fwhm/2.35482 # 2.35482approx.(2*np.sqrt(2*np.log(2)))
        tmp = element.dr_strength * _normpdf(e_kin, element.dr_e_res, sig)*1e-24
        for k in range(element.dr_cs.size):
            # cs = int(element.dr_cs[k])
            xs_vec[element.dr_cs[k]] = xs_vec[element.dr_cs[k]] + tmp[k]
    return xs_vec


@numba.njit
def drxs_mat(element, e_kin, fwhm):
    """
    Dielectronic recombination cross section.
    The cross sections are estimated by weighing the strength of each transition with the
    profile of a normal Gaussian distribution. This simulates the effective spreading of the
    resonance peaks due to the energy spread of the electron beam

    Parameters
    ----------
    element : ebisim.Element
        An ebisim.Element object that holds the required physical information for cross section
        calculations.
    e_kin : float
        <Unit: eV>
        Kinetic energy of the impacting electron.
    fwhm : float
        <Unit: eV>
        Energy spread to apply for the resonance smearing, expressed in terms of
        full width at half maximum.

    Returns
    -------
    out : numpy.array
        <Unit m^2>
        The cross sections for each individual charge state, arranged in a matrix suitable
        for implementation of a rate equation like dN/dt = j * xs_matrix dot N.
        out[q, q]   = - cross section of q+ ion
        out[q, q+1] = + cross section of (q+1)+ ion

    See Also
    --------
    ebisim.drxs_vec : Similar method with different output format.

    """
    xs = drxs_vec(element, e_kin, fwhm)
    return np.diag(xs[1:], 1) - np.diag(xs)


@numba.jit
def precompute_rr_quantities(cfg, shell_n):
    """
    Precomputes the effective valence shell and nuclear charge for all charge states,
    as required for the computation of radiative recombinations cross sections.
    According to the procedure described in [1]_.

    Parameters
    ----------
    cfg : numpy.ndarray
        Matrix holding the number of electrons in each shell.
        The row index corresponds to the charge state, the columns to different subshells
    shell_n : numpy.ndarray
        Array holding the main quantum number n corresponding to each shell listed in cfg

    Returns
    -------
    z_eff : numpy.ndarray
        Array holding the effective nuclear charge for each charge state,
        where the array-index corresponds to the charge state.
    n_0_eff : numpy.ndarray
        Array holding the effective valence shell number for each charge state,
        where the array-index corresponds to the charge state.

    References
    ----------
    .. [1] "Direct radiative recombination of electrons with atomic ions:
           Cross sections and rate coefficients",
           Young Soon Kim and R. H. Pratt,
           Phys. Rev. A 27, 2913 (1983),
           https://journals.aps.org/pra/abstract/10.1103/PhysRevA.27.2913

    See Also
    --------
    ebisim.rrxs_vec
    ebisim.rrxs_mat

    """
    z = cfg.shape[0]
    shell_n = shell_n[:cfg.shape[1]] # Crop shell_n to the shells described in cfg

    n_0 = np.zeros(z + 1)
    occup = np.zeros(z + 1)

    # Determine, for each charge state, the valence shell (n_0),
    # and the number of electrons in it (occup)
    # Fully ionised
    n_0[z] = 1
    occup[z] = 0
    # All other charge states
    for cs in range(z):
        conf = cfg[cs, :]
        n_0[cs] = np.max(shell_n[np.nonzero(conf)])
        occup[cs] = np.sum(np.extract((shell_n == n_0[cs]), conf))

    w_n0 = (2 * n_0**2 - occup) / (2 * n_0**2)
    n_0_eff = n_0 + (1 - w_n0) - 0.3
    z_eff = (z + np.arange(z + 1)) / 2

    n_0_eff.setflags(write=False)
    z_eff.setflags(write=False)
    return z_eff, n_0_eff
