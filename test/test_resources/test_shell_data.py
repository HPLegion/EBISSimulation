"""
Tests for ebisim.resources._shell_data
"""

import pytest
import numpy as np
from ebisim.resources import SHELL_CFG, SHELL_EBIND, SHELL_N, SHELL_ORDER

def test_shell_order():
    assert SHELL_ORDER == (
        '1s', '2s', '2p-', '2p+', '3s', '3p-', '3p+', '3d-', '3d+', '4s', '4p-', '4p+', '4d-',
        '4d+', '4f-', '4f+', '5s', '5p-', '5p+', '5d-', '5d+', '5f-', '5f+', '6s', '6p-', '6p+',
        '6d-', '6d+', '7s', '7p-'
    )

def test_shell_n():
    assert np.any(
        SHELL_N == np.array((
            1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7
        ))
    )


def test_configuration():
    assert np.any(SHELL_CFG[1] == _H_CFG)
    assert np.any(SHELL_CFG[3] == _LI_CFG)
    assert np.any(SHELL_CFG[105] == _DB_CFG)

def test_bdining_energies():
    assert np.any(SHELL_EBIND[1] == _H_EBIND)
    assert np.any(SHELL_EBIND[3] == _LI_EBIND)
    assert np.any(SHELL_EBIND[105] == _DB_EBIND)

# Manually written arrays
_H_CFG = np.array([[1]])
_H_EBIND = np.array([[1.35984487E+01]])
_LI_CFG = np.array([
    [2, 1],
    [2, 0],
    [1, 0]
])
_LI_EBIND = np.array([
    [6.31453715E+01, 5.13703653E+00],
    [7.44476435E+01, 0],
    [1.22454941E+02, 0]
])
_DB_CFG = np.array([
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 3, 0, 2],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 3, 0, 1],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 3, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 2, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 1, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 7, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 6, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 5, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 4, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 3, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 2, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 1, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 6, 0, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 5, 0, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 4, 0, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 3, 0, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 2, 0, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 1, 0, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 0, 0, 2, 2, 4, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 0, 0, 2, 2, 3, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 0, 0, 2, 2, 2, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 0, 0, 2, 2, 1, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 0, 0, 2, 2, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 0, 0, 2, 1, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 0, 0, 2, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 0, 0, 1, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 8, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 7, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 6, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 5, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 4, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 3, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 2, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 1, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 6, 0, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 5, 0, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 4, 0, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 3, 0, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 2, 0, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 1, 0, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 0, 0, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 0, 0, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

_DB_EBIND = np.array([
    [160495.06, 31837.0689, 30861.1565, 23363.3387, 8442.68663, 7987.74002, 6186.08602, 5474.73875, 5148.13662, 2353.49304, 2137.7548, 1631.99754, 1291.21724, 1204.35414, 751.786597, 727.445646, 574.906451, 481.86768, 345.789634, 207.505109, 186.787845, 27.6196513, 23.3426742, 92.3473902, 62.3940208, 33.7621079, 6.24120304, 0, 6.8456614],
    [160503.162, 31845.2203, 30869.3368, 23371.5089, 8450.76606, 7995.86309, 6194.23695, 5482.8475, 5156.26183, 2361.4345, 2145.77758, 1640.04842, 1299.26388, 1212.43495, 759.836345, 735.515207, 582.83522, 489.935898, 353.864427, 215.586139, 194.913992, 35.6392885, 31.4761519, 99.9069579, 70.3003639, 41.3802664, 13.9894506, 0, 15.8676695],
    [160512.257, 31854.302, 30878.3927, 23380.5559, 8459.84458, 8004.92561, 6203.2797, 5491.89382, 5165.28936, 2370.46401, 2154.79423, 1649.01869, 1308.26898, 1221.39667, 768.84807, 744.493119, 591.852879, 498.927177, 362.723856, 224.487052, 203.724294, 44.5476573, 40.2181046, 108.897251, 79.3372578, 50.0762405, 21.9291676, 0, 0],
    [160524.634, 31866.6802, 30890.7144, 23392.8986, 8472.11349, 8017.18118, 6215.55459, 5504.12915, 5177.58021, 2382.69997, 2166.98286, 1661.27265, 1320.41699, 1233.68411, 781.038273, 756.781711, 604.118208, 511.041723, 374.98118, 236.571971, 216.072723, 56.555806, 52.5091464, 121.128873, 90.4483186, 61.4800434, 32.9309214, 0, 0],
    [160538.223, 31880.3315, 30904.3205, 23406.4413, 8485.65371, 8030.71305, 6228.95455, 5517.64626, 5191.01088, 2396.17889, 2180.43872, 1674.47776, 1333.85395, 1246.91752, 794.42733, 770.048758, 617.572568, 524.412703, 387.88644, 249.931845, 228.982085, 69.6350265, 65.2800326, 134.467065, 102.892682, 73.4699717, 43.9484233, 0, 0],
    [160552.971, 31895.083, 30919.0594, 23421.2603, 8500.19817, 8045.2618, 6243.64644, 5532.24042, 5205.68693, 2410.65409, 2194.91916, 1689.25794, 1348.39025, 1261.65615, 808.974556, 784.740415, 632.024649, 538.864618, 402.996539, 264.54685, 244.129011, 84.2303704, 80.5314282, 148.814483, 117.007113, 88.7344253, 0, 0, 0],
    [160576.337, 31918.7135, 30942.5759, 23444.7771, 8524.11349, 8069.33134, 6267.35737, 5555.83627, 5228.65675, 2434.48038, 2218.80735, 1712.22279, 1371.21888, 1284.4811, 832.177768, 805.891625, 654.819368, 561.98977, 424.246052, 284.807586, 260.51246, 104.081544, 100.599065, 167.887534, 135.481529, 105.50028, 0, 0, 0],
    [160600.704, 31943.5683, 30967.3471, 23469.67, 8549.30976, 8094.72369, 6292.28474, 5581.36865, 5253.43238, 2459.53742, 2243.96576, 1737.34395, 1396.32691, 1309.35814, 857.065759, 830.588848, 678.660062, 586.345783, 446.484125, 308.044902, 281.074983, 125.324242, 121.999443, 187.65551, 154.769829, 123.218412, 0, 0, 0],
    [160626.228, 31969.6355, 30993.3064, 23495.7358, 8575.74371, 8121.35549, 6318.4249, 5608.27122, 5279.58863, 2485.75511, 2270.28446, 1763.87665, 1422.91269, 1335.91749, 884.251564, 857.126682, 703.518842, 611.728394, 469.796867, 327.855493, 303.659695, 148.830129, 145.561203, 208.106111, 174.74665, 141.242069, 0, 0, 0],
    [160652.861, 31996.8383, 31020.3872, 23522.8929, 8603.37274, 8149.14095, 6345.79127, 5636.24018, 5306.94607, 2513.07719, 2297.68957, 1790.98156, 1450.34912, 1362.77381, 912.275855, 884.085715, 729.385338, 638.095855, 494.284542, 354.815573, 327.425569, 173.513669, 170.565584, 229.252394, 195.398717, 159.885498, 0, 0, 0],
    [160680.589, 32025.1967, 31048.6129, 23551.2316, 8632.16751, 8178.11537, 6374.4311, 5664.90544, 5335.58331, 2541.49817, 2326.2005, 1818.89251, 1478.07699, 1390.48248, 929.262678, 911.827571, 756.108375, 665.286332, 519.905334, 369.331623, 352.268364, 197.398726, 195.088492, 250.966495, 216.643703, 179.181391, 0, 0, 0],
    [160707.989, 32054.466, 31077.9704, 23580.8349, 8662.07041, 8208.1646, 6404.40103, 5694.73397, 5365.62513, 2570.95519, 2355.75167, 1848.13161, 1507.31336, 1419.63579, 958.64416, 941.070195, 783.561619, 692.95287, 546.757541, 395.412879, 378.528105, 224.810591, 219.838401, 273.155646, 238.280983, 199.245433, 0, 0, 0],
    [160739.524, 32085.4918, 31108.5681, 23611.7176, 8693.2306, 8239.24411, 6435.81673, 5725.33616, 5397.29571, 2601.48139, 2386.26859, 1878.90476, 1538.12252, 1450.57891, 990.238151, 972.276714, 811.745712, 720.895042, 575.000553, 423.304178, 406.585964, 249.84016, 247.219409, 295.825084, 260.126702, 220.243709, 0, 0, 0],
    [160769.875, 32116.6106, 31139.4606, 23642.9418, 8725.81797, 8271.6173, 6468.55557, 5758.88929, 5429.85497, 2633.14364, 2417.73939, 1910.32239, 1569.9447, 1482.07014, 1023.77412, 1004.097, 843.126054, 753.070958, 606.224973, 450.779712, 436.619417, 278.996039, 0, 320.89274, 284.238782, 242.47856, 0, 0, 0],
    [160802.073, 32149.6155, 31172.2958, 23675.8442, 8759.1171, 8304.69234, 6501.5133, 5791.01601, 5462.93398, 2665.6429, 2450.18997, 1941.74145, 1601.80655, 1513.4123, 1053.34017, 1035.66766, 873.243168, 781.452919, 634.548757, 483.780114, 463.960402, 305.316163, 0, 344.620386, 306.570164, 263.402527, 0, 0, 0],
    [160835.229, 32183.6009, 31206.1108, 23709.9838, 8793.72835, 8338.89724, 6536.23257, 5824.82351, 5497.71702, 2699.26468, 2483.61049, 1975.35818, 1635.13302, 1546.66614, 1086.08562, 1068.99144, 904.666014, 811.132717, 664.817391, 509.818495, 493.178625, 333.937417, 0, 369.30739, 329.732191, 285.791758, 0, 0, 0],
    [160869.316, 32218.5339, 31240.8635, 23744.884, 8829.44293, 8374.20902, 6571.84363, 5859.98652, 5533.7073, 2733.83701, 2517.97154, 2009.73309, 1669.01638, 1581.37095, 1120.83157, 1103.96513, 937.116391, 841.999093, 695.557141, 539.915115, 523.697329, 364.149561, 0, 394.693388, 353.666634, 308.513751, 0, 0, 0],
    [160904.387, 32254.4674, 31276.602, 23780.8016, 8866.15444, 8410.65761, 6607.7887, 5896.35037, 5569.68248, 2769.31643, 2553.3269, 2043.83066, 1703.66581, 1615.38973, 1154.7448, 1138.41374, 970.270014, 873.97757, 726.160756, 572.099972, 553.179396, 393.133155, 0, 420.533597, 378.308516, 330.983217, 0, 0, 0],
    [160940.452, 32291.4319, 31313.3471, 23817.8435, 8903.84109, 8448.28053, 6645.12178, 5933.98034, 5606.3267, 2805.65194, 2589.6555, 2079.46083, 1739.55492, 1649.69147, 1198.66024, 1173.02784, 1004.08941, 907.195786, 758.491953, 610.043189, 582.556641, 421.633892, 0, 446.80397, 403.669222, 354.498099, 0, 0, 0],
    [160977.462, 32329.381, 31351.0591, 23856.0433, 8942.57797, 8487.07406, 6685.05877, 5973.24286, 5646.91145, 2842.89638, 2626.955, 2118.17184, 1777.18143, 1689.71781, 1237.70117, 1213.19396, 1038.8289, 941.688868, 794.973138, 643.842225, 620.424566, 0, 0, 473.663377, 429.727315, 380.469981, 0, 0, 0],
    [161006, 32357.4143, 31379.3017, 23883.7248, 8969.89071, 8514.54816, 6712.02726, 6000.46732, 5674.25376, 2869.38907, 2653.67786, 2144.2241, 1803.27233, 1716.00437, 1263.78853, 1239.4209, 1063.63513, 966.916026, 818.781259, 667.623572, 644.631961, 0, 0, 492.23217, 450.276569, 400.909545, 0, 0, 0],
    [161035.159, 32386.0172, 31408.1281, 23912.3054, 8997.76551, 8542.57646, 6739.82379, 6028.66149, 5702.19008, 2896.46916, 2680.9522, 2171.09578, 1830.72695, 1743.15173, 1291.35031, 1266.89921, 1089.11669, 992.733209, 843.796723, 693.16858, 669.531273, 0, 0, 512.32726, 472.301564, 423.815502, 0, 0, 0],
    [161064.947, 32415.1622, 31437.4891, 23941.3763, 9026.19901, 8571.11658, 6768.10833, 6056.67694, 5730.4956, 2924.13686, 2708.71493, 2198.46284, 1857.43834, 1770.379, 1318.32317, 1294.15242, 1115.29652, 1019.02731, 869.342099, 717.414021, 694.508251, 0, 0, 534.114223, 494.788697, 444.817952, 0, 0, 0],
    [161095.375, 32444.8727, 31467.4237, 23971.1398, 9055.20934, 8600.19834, 6797.15503, 6086.25753, 5759.63693, 2952.43283, 2737.02787, 2226.76648, 1886.67596, 1798.75954, 1347.3234, 1322.61426, 1142.24828, 1045.91107, 896.116563, 745.569142, 721.126127, 0, 0, 557.946129, 518.200887, 0, 0, 0, 0],
    [161129.614, 32477.5634, 31499.7249, 24003.793, 9086.89224, 8631.38139, 6828.77567, 6117.90986, 5791.38616, 2983.06006, 2766.9656, 2257.23076, 1917.022, 1829.28911, 1377.88653, 1353.27419, 1170.72877, 1073.0036, 924.124135, 772.638999, 748.794064, 0, 0, 578.165586, 543.293598, 0, 0, 0, 0],
    [161164.761, 32511.0084, 31533.4807, 24037.152, 9119.33625, 8663.9412, 6861.1044, 6150.36755, 5823.78389, 3014.57406, 2798.52659, 2288.49992, 1948.32968, 1860.53842, 1409.21969, 1384.58031, 1200.48522, 1102.66702, 953.273681, 801.505696, 777.533693, 0, 0, 604.011452, 0, 0, 0, 0, 0],
    [161199.698, 32544.6693, 31567.7885, 24071.1796, 9152.04967, 8697.19187, 6894.17307, 6183.68536, 5857.04726, 3046.02954, 2830.6372, 2320.28567, 1980.35702, 1892.47353, 1441.38172, 1416.70545, 1229.02059, 1132.31125, 981.972328, 830.244928, 805.980773, 0, 0, 630.518905, 0, 0, 0, 0, 0],
    [161235.924, 32579.4957, 31602.8401, 24105.923, 9186.0066, 8731.23711, 6928.01312, 6217.6556, 5890.96352, 3079.03964, 2863.68404, 2353.01962, 2013.14877, 1925.18511, 1474.19979, 1449.48876, 1260.09742, 1163.30464, 1012.31948, 860.327058, 835.883145, 0, 0, 0, 0, 0, 0, 0, 0],
    [161283.76, 32627.0095, 31650.9972, 24152.5637, 9232.10487, 8777.66805, 6973.43114, 6263.22814, 5934.94574, 3122.42231, 2907.47299, 2395.43715, 2055.00287, 1964.28505, 1515.97847, 1491.10593, 1296.70123, 1201.20883, 1041.04819, 894.436794, 870.50846, 0, 0, 0, 0, 0, 0, 0, 0],
    [161332.416, 32675.3957, 31699.952, 24200.5721, 9278.92573, 8824.81559, 7020.12388, 6310.872, 5981.94918, 3166.50163, 2951.99596, 2439.16761, 2099.58536, 2008.21681, 1560.01533, 1535.25953, 1334.12731, 1240.35121, 1074.13243, 931.306585, 907.339521, 0, 0, 0, 0, 0, 0, 0, 0],
    [161381.892, 32724.7132, 31749.6744, 24249.7446, 9326.49207, 8872.6577, 7067.28908, 6359.27569, 6029.50612, 3211.32434, 2997.15746, 2483.15116, 2145.32911, 2052.64525, 1605.1673, 1579.92412, 1372.59252, 1280.31667, 1110.05828, 969.677572, 946.583515, 0, 0, 0, 0, 0, 0, 0, 0],
    [161432.202, 32774.9865, 31800.1841, 24299.959, 9374.81139, 8921.20023, 7115.01865, 6407.18113, 6077.53371, 3256.90217, 3042.9709, 2527.63719, 2189.44117, 2096.76058, 1649.87465, 1624.18869, 1412.0583, 1321.07692, 1147.54009, 1005.94594, 984.217973, 0, 0, 0, 0, 0, 0, 0, 0],
    [161483.327, 32826.2187, 31851.4534, 24351.2459, 9423.87047, 8970.42507, 7163.76943, 6456.17816, 6126.49406, 3303.24825, 3089.41453, 2573.27216, 2235.33422, 2141.72864, 1694.15147, 1670.05106, 1452.68123, 1362.52097, 1186.40749, 1044.41645, 1020.89158, 0, 0, 0, 0, 0, 0, 0, 0],
    [161535.245, 32878.5332, 31903.526, 24403.9267, 9473.72135, 9020.34745, 7213.83402, 6507.41983, 6177.49765, 3350.51343, 3136.60837, 2620.54571, 2284.74843, 2190.04375, 1744.13041, 1718.03618, 1495.07963, 1405.33577, 1228.02179, 1087.23158, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [161589.358, 32932.3637, 31956.9777, 24457.4919, 9524.96831, 9071.54444, 7263.89516, 6556.84273, 6227.93434, 3398.15585, 3183.47158, 2666.31155, 2327.399, 2235.56539, 1789.33135, 1763.93514, 1534.61038, 1438.32828, 1265.75679, 1125.45327, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [161644.399, 32987.1758, 32011.5887, 24512.6314, 9577.01794, 9123.61818, 7316.21671, 6608.77544, 6280.80148, 3446.858, 3231.48666, 2714.93082, 2374.83249, 2284.26815, 1839.30801, 1813.03539, 1576.44622, 1474.86602, 1305.53747, 1167.25347, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [161700.411, 33042.8064, 32067.406, 24567.6656, 9629.78065, 9176.60846, 7367.06381, 6661.42909, 6332.58069, 3496.27801, 3280.69103, 2761.20047, 2423.01673, 2331.2002, 1887.47684, 1860.62612, 1619.30496, 1515.12263, 1343.29441, 1205.9656, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [161757.396, 33099.2483, 32124.4479, 24624.8686, 9683.27189, 9230.51601, 7422.10501, 6715.88945, 6387.71292, 3546.53514, 3331.09801, 2814.00698, 2473.41469, 2383.54891, 1938.36523, 1912.82489, 1663.7826, 1559.30591, 1390.17936, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [161843.551, 33187.9673, 32212.8955, 24713.1199, 9771.67478, 9320.48372, 7507.6731, 6802.23153, 6467.84523, 3621.90141, 3408.47899, 2883.81672, 2544.39138, 2443.34385, 2010.71401, 1985.88682, 1718.42927, 1613.75677, 1439.20377, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [161931.354, 33278.2782, 32302.8401, 24803.7141, 9861.66718, 9412.18474, 7594.64314, 6894.47741, 6554.51743, 3698.4526, 3487.46917, 2954.7844, 2621.36549, 2511.82893, 2086.03195, 2061.55904, 1773.7524, 1668.96627, 1490.18656, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [162020.624, 33370.1337, 32394.2539, 24895.7677, 9953.33883, 9505.40884, 7683.36731, 6989.37035, 6644.18355, 3776.33829, 3567.65337, 3027.15826, 2702.2059, 2583.73017, 2167.28287, 2142.552, 1829.78383, 1724.85565, 1542.25599, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [162111.341, 33463.5175, 32487.1089, 24988.8349, 10046.8501, 9600.14897, 7774.19145, 7085.64892, 6735.75098, 3855.81012, 3649.07044, 3101.20908, 2780.73537, 2657.36105, 2251.48978, 2227.55169, 1886.58165, 1781.43926, 1594.11081, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [162203.546, 33558.4776, 32581.4548, 25083.5941, 10142.1079, 9696.43237, 7867.25708, 7179.69674, 6829.44671, 3936.63228, 3731.67888, 3176.95974, 2859.63109, 2732.72266, 2331.57396, 2309.72646, 1944.09815, 1838.71478, 1646.38779, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [162297.233, 33655.0134, 32677.2873, 25180.2402, 10239.0756, 9794.19655, 7963.04008, 7276.40603, 6926.0913, 4018.72123, 3815.30617, 3254.81903, 2941.65164, 2810.57869, 2410.17705, 2390.24456, 2002.31553, 1896.65135, 1699.73454, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [162392.368, 33753.0748, 32774.5439, 25278.8614, 10338.0905, 9893.4727, 8062.22175, 7376.11287, 7026.43254, 4102.61882, 3900.04816, 3335.49074, 3021.61203, 2891.74093, 2494.93125, 2471.38199, 2061.35281, 1955.24023, 1754.46328, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [162488.778, 33852.5702, 32873.078, 25379.3569, 10440.2751, 9994.9169, 8166.08211, 7483.32803, 7131.47158, 4190.20144, 3987.41216, 3420.46532, 3109.50622, 2977.64123, 2591.70193, 0, 2121.58422, 2014.68584, 1810.84469, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [162588.059, 33954.9214, 32974.8497, 25480.8998, 10541.1637, 10093.9643, 8262.90402, 7573.78628, 7229.79856, 4273.34838, 4067.04888, 3497.26323, 3178.0882, 3054.67944, 2673.7088, 0, 2180.97615, 2073.52531, 1864.24133, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [162688.893, 34058.8455, 33078.1533, 25585.6099, 10644.6085, 10195.3593, 8365.98742, 7671.61621, 7333.38179, 4359.08252, 4149.2698, 3579.20758, 3247.79341, 3136.2139, 2761.4739, 0, 2241.44016, 2133.25759, 1921.00006, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [162791.21, 34164.2816, 33182.9322, 25690.9178, 10750.1737, 10299.1596, 8471.58209, 7774.09322, 7441.69475, 4446.82407, 4234.14082, 3662.90116, 3326.6852, 3221.58805, 2854.96735, 0, 2302.77804, 2193.90254, 1978.31352, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [162895.107, 34271.3513, 33289.2778, 25797.737, 10857.3407, 10405.4104, 8573.3761, 7879.61028, 7546.27875, 4535.78102, 4321.56584, 3743.25483, 3410.1991, 3303.01459, 2943.51667, 0, 2364.79427, 2255.46187, 2033.94526, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [163000.579, 34380.0616, 33397.1895, 25906.7513, 10965.9607, 10514.1944, 8679.64111, 7988.2666, 7648.86482, 4625.76522, 4411.58887, 3827.28901, 3496.45899, 3382.21844, 3029.24615, 0, 2427.42953, 2317.92603, 2091.14562, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [163106.222, 34490.1247, 33506.6065, 26018.4132, 11076.4608, 10625.5367, 8796.60345, 8102.26801, 7770.64506, 4717.50987, 4504.21425, 3921.04278, 3587.97059, 3482.24948, 0, 0, 2490.83986, 2381.27701, 2153.06253, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [163178.395, 34558.8774, 33576.7668, 26085.1355, 11140.0451, 10690.2002, 8858.21497, 8165.71423, 7834.44035, 4774.5612, 4562.62922, 3975.04185, 3643.81484, 3538.96712, 0, 0, 2531.67642, 2427.91985, 2199.33332, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [163253.2, 34628.7766, 33647.6722, 26154.5289, 11204.6532, 10755.6506, 8922.19202, 8231.78234, 7899.12733, 4832.82531, 4621.98535, 4032.2947, 3703.12797, 3596.59696, 0, 0, 2576.11494, 2477.02482, 2250.30352, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [163327.979, 34699.2901, 33719.2612, 26224.5982, 11270.1653, 10821.7509, 8986.69258, 8295.80489, 7964.0506, 4892.29121, 4682.02163, 4090.11154, 3759.33934, 3654.30233, 0, 0, 2624.3607, 2527.26944, 2297.21426, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [163404.073, 34770.7122, 33791.5575, 26296.4912, 11336.6905, 10888.6306, 9053.20165, 8364.70728, 8031.28786, 4953.05195, 4742.9916, 4150.51596, 3823.45969, 3715.20235, 0, 0, 2676.72482, 2579.60973, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [163490.291, 34849.1405, 33867.7379, 26374.3969, 11408.5092, 10958.0337, 9124.32836, 8436.22862, 8103.31207, 5016.87568, 4803.09262, 4213.26335, 3885.84403, 3778.54287, 0, 0, 2720.39403, 2635.21199, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [163579.783, 34928.504, 33949.272, 26453.1517, 11481.5781, 11032.0972, 9196.61711, 8509.76393, 8176.21458, 5082.99272, 4869.63717, 4277.98102, 3951.23966, 3843.41378, 0, 0, 2776.26179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [163661.172, 35004.0092, 34028.3152, 26530.231, 11551.3374, 11104.5086, 9267.64364, 8582.34911, 8248.31169, 5143.89601, 4934.01694, 4340.35272, 4015.21178, 3906.7991, 0, 0, 2832.50288, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [163748.244, 35083.3635, 34108.0786, 26608.9918, 11624.9973, 11178.5429, 9340.49154, 8656.07962, 8321.80957, 5210.66878, 5001.02002, 4405.65497, 4081.09979, 3972.29762, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [163868.321, 35200.5293, 34228.5865, 26722.0876, 11732.0478, 11287.593, 9444.16226, 8761.6529, 8418.21285, 5293.36035, 5088.5739, 4473.16432, 4162.73537, 4054.93089, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [163989.862, 35319.5542, 34350.4168, 26839.3476, 11840.2836, 11397.7372, 9550.64354, 8873.40774, 8527.01184, 5378.06797, 5178.45226, 4550.09831, 4250.49878, 4142.13749, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [164112.845, 35440.5633, 34473.481, 26959.5721, 11949.7587, 11508.8759, 9657.63029, 8987.62976, 8636.69257, 5465.15007, 5269.80517, 4632.5436, 4341.70402, 4234.878, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [164237.294, 35563.5981, 34597.7999, 27082.1136, 12060.4877, 11621.0214, 9765.06534, 9097.62897, 8746.29916, 5554.60418, 5362.61551, 4717.89149, 4426.9865, 4323.25125, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [164363.231, 35688.7099, 34723.3816, 27207.2337, 12172.4847, 11734.1699, 9874.88902, 9210.92478, 8857.27569, 5646.57186, 5456.80562, 4805.94785, 4516.909, 4408.90337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [164490.611, 35816.1012, 34850.3049, 27336.2847, 12285.8449, 11848.3952, 9988.49504, 9331.94074, 8976.36997, 5741.58633, 5553.34477, 4899.32235, 4616.95811, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [164623.378, 35946.4006, 34979.1308, 27465.0284, 12401.2044, 11963.6736, 10098.1805, 9434.50546, 9088.44079, 5829.4689, 5628.76255, 4984.15815, 4706.46165, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [164758.153, 36078.5968, 35110.9511, 27598.7693, 12518.0173, 12080.968, 10214.5992, 9551.3749, 9207.91196, 5922.10178, 5712.17419, 5073.39104, 4804.26807, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [164894.941, 36212.2098, 35245.8267, 27729.8651, 12635.9439, 12200.3184, 10325.0867, 9669.32881, 9323.23522, 6017.02837, 5803.72492, 5157.97652, 4894.8089, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [165033.766, 36347.3176, 35383.8146, 27868.0522, 12755.1294, 12321.731, 10449.5278, 9793.00601, 9449.23682, 6115.71722, 5903.60068, 5261.40585, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [165172.726, 36475.299, 35516.1736, 27989.9737, 12865.7197, 12436.1289, 10552.7264, 9904.25756, 9561.43867, 6191.6428, 5992.08874, 5348.25099, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [165314.398, 36604.9851, 35649.6704, 28118.9318, 12978.5113, 12552.0923, 10664.0597, 10021.4389, 9674.47984, 6274.52968, 6084.75022, 5443.47196, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [165458.96, 36736.3755, 35784.3821, 28248.9841, 13093.5462, 12669.234, 10776.1084, 10133.2801, 9788.20967, 6364.69119, 6179.59726, 5531.32349, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [165606.327, 36869.525, 35920.2435, 28383.371, 13210.9106, 12787.9379, 10893.1533, 10257.5431, 9907.7477, 6462.48232, 6278.33546, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [165778.049, 37017.7478, 36062.0484, 28530.0297, 13337.0213, 12905.3034, 11017.0456, 10383.0542, 10035.0651, 6545.2416, 6384.62956, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [165958.087, 37167.7037, 36218.6029, 28678.1832, 13466.4868, 13037.9587, 11144.0034, 10514.3808, 10164.3346, 6650.16513, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [166112.472, 37304.0608, 36365.4667, 28819.0801, 13582.1362, 13163.01, 11264.2701, 10640.3721, 10288.7132, 6754.6131, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [166281.848, 37450.6683, 36513.5727, 28963.9316, 13710.3442, 13292.5882, 11389.9169, 10769.2051, 10416.7322, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [166536.907, 37693.6799, 36768.33, 29191.2647, 13894.4416, 13491.961, 11547.2834, 10961.2508, 10609.0807, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [166795.181, 37941.3217, 37025.8549, 29431.7842, 14082.994, 13695.5358, 11721.0792, 11169.5249, 10813.4691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [167056.655, 38193.9951, 37285.9038, 29680.9647, 14276.5485, 13901.9304, 11904.444, 11385.3943, 11032.1977, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [167321.391, 38451.8139, 37548.5063, 29936.4181, 14475.1162, 14111.123, 12093.3612, 11587.022, 11239.498, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [167589.402, 38714.9337, 37813.6912, 30199.0897, 14678.8343, 14323.0442, 12288.1925, 11798.0174, 11438.9809, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [167860.69, 38983.8815, 38081.7205, 30473.7433, 14888.4088, 14539.1184, 12494.1829, 12032.0203, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [168146.484, 39259.3588, 38352.4282, 30742.5445, 15086.2803, 14717.8856, 12683.5299, 12245.2532, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [168437.279, 39539.1671, 38631.5103, 31027.7917, 15292.6524, 14913.1705, 12884.3688, 12480.4197, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [168733.171, 39822.0146, 38919.179, 31301.1095, 15503.4329, 15125.0956, 13073.3618, 12696.7473, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [169034.241, 40108.2635, 39215.6542, 31598.3685, 15721.1824, 15353.8359, 13298.5842, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [169326.636, 40360.4835, 39484.3973, 31827.461, 15881.6923, 15547.1553, 13483.9321, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [169626.113, 40617.2015, 39755.2212, 32082.2198, 16057.2615, 15748.0231, 13686.6871, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [169933.168, 40878.4497, 40028.3828, 32339.1217, 16248.413, 15953.5852, 13874.1045, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [170247.568, 41144.3355, 40303.6798, 32608.9203, 16455.6179, 16166.9281, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [170632.24, 41446.1383, 40579.5629, 32905.5352, 16638.5916, 16405.2832, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [171042.969, 41751.8109, 40909.6797, 33205.1998, 16863.6953, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [171362.842, 42005.3233, 41202.087, 33476.5258, 17083.6393, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [171729.932, 42295.2242, 41498.0439, 33760.583, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [172406.971, 42721.2818, 42054.7943, 34258.0878, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [173106.444, 43186.3516, 42621.5105, 34811.4633, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [173830.198, 43691.715, 43196.9421, 35315.8852, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [174577.456, 44238.1461, 43782.4373, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [175584.621, 44781.7547, 44537.1795, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [176706.816, 45390.538, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [177422.874, 45971.9174, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [178336.11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [181271.916, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])