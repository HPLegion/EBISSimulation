"""
This subpackage contains functions and classes provide an interface to run simulations and inspect
their results.
"""

from ._result import BasicResult, AdvancedResult, Rate

from ._basic import basic_simulation

from ._advanced import (
    advanced_simulation,
    Device,
    ModelOptions,
    BackgroundGas,
    AdvancedModel,
)

from ._energyscan import (
    energy_scan,
    EnergyScanResult,
)

from ._radial_dist import (
    tridiagonal_matrix_algorithm,
    fd_system_uniform_grid,
    radial_potential_uniform_grid,
    fd_system_nonuniform_grid,
    radial_potential_nonuniform_grid,
    boltzmann_radial_potential_onaxis_density,
    boltzmann_radial_potential_linear_density,
    boltzmann_radial_potential_linear_density_ebeam,
    heat_capacity,
)

__all__ = [
    "BasicResult",
    "AdvancedResult",
    "Rate",
    "basic_simulation",
    "advanced_simulation",
    "Device",
    "ModelOptions",
    "BackgroundGas",
    "AdvancedModel",
    "energy_scan",
    "EnergyScanResult",
    "tridiagonal_matrix_algorithm",
    "fd_system_uniform_grid",
    "radial_potential_uniform_grid",
    "fd_system_nonuniform_grid",
    "radial_potential_nonuniform_grid",
    "boltzmann_radial_potential_onaxis_density",
    "boltzmann_radial_potential_linear_density",
    "boltzmann_radial_potential_linear_density_ebeam",
    "heat_capacity",
]
