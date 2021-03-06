"""
Tests for ebisim.elements
"""
import pytest
from ebisim.elements import (
    element_name,
    element_symbol,
    element_z,
    Element,
    get_element
)

def test_element_z():
    assert element_z("K") == 19
    assert element_z("Potassium") == 19
    assert element_z("Cs") == 55
    assert element_z("Caesium") == 55
    assert element_z("U") == 92
    assert element_z("Uranium") == 92

def test_element_symbol():
    assert element_symbol(19) == "K"
    assert element_symbol("Potassium") == "K"
    assert element_symbol(55) == "Cs"
    assert element_symbol("Caesium") == "Cs"
    assert element_symbol(92) == "U"
    assert element_symbol("Uranium") == "U"

def test_element_name():
    assert element_name(19) == "Potassium"
    assert element_name("K") == "Potassium"
    assert element_name(55) == "Caesium"
    assert element_name("Cs") == "Caesium"
    assert element_name(92) == "Uranium"
    assert element_name("U") == "Uranium"

def test_Element_basic_info():
    # Test some elements
    k = [19, "K", "Potassium", 39]
    cs = [55, "Cs", "Caesium", 133]
    u = [92, "U", "Uranium", 238]
    for elem_ref in [k, cs, u]:
        for idx in elem_ref[:-1]:
            elem = get_element(idx)
            assert elem.z == elem_ref[0]
            assert elem.symbol == elem_ref[1]
            assert elem.name == elem_ref[2]
            assert elem.a == elem_ref[3]
    # Check that meaningless elements throw ValueErrors
    with pytest.raises(ValueError):
        get_element(0)
    with pytest.raises(ValueError):
        get_element(106)
    with pytest.raises(ValueError):
        get_element("h")
    with pytest.raises(ValueError):
        get_element("HE")
    with pytest.raises(ValueError):
        get_element("XX")
    with pytest.raises(ValueError):
        get_element("Ccarbon")

def test_Element_mass_number():
    # test overwriting of the defaults of a
    for z in [12, 15, 55]:
        for a_ref in [1, 12, 54, 23, 77]:
            assert get_element(z, a=a_ref).a == a_ref
    # test that meaningless a raise an Error
    with pytest.raises(ValueError):
        get_element(1, a=-1)
    with pytest.raises(ValueError):
        get_element(1, a=0)
    with pytest.raises(TypeError):
        get_element(1, a="x")
