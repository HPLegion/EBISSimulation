"""
Tests for ebisim.resources._element_data
"""

import pytest

from ebisim.resources import ELEMENT_Z, ELEMENT_ES, ELEMENT_NAME, ELEMENT_A, ELEMENT_IP

def test_tuple_extents():
    assert len(ELEMENT_Z)    == 105
    assert len(ELEMENT_ES)   == 105
    assert len(ELEMENT_NAME) == 105
    assert len(ELEMENT_A)    == 105
    assert len(ELEMENT_IP)   == 105

    assert min(ELEMENT_Z) == 1
    assert max(ELEMENT_Z) == 105

    assert min(ELEMENT_A) == 1
    assert max(ELEMENT_A) == 262

    assert min(ELEMENT_IP) == pytest.approx(3.893905695)
    assert max(ELEMENT_IP) == pytest.approx(24.5873888)

def test_alignment():
    #Random handpicked test cases
    idxs = [0, 5, 27, 54, 94, 103]
    Z = [1, 6, 28, 55, 95, 104]
    ES = ["H", "C", "Ni", "Cs", "Am", "Rf"]
    NAME = ["Hydrogen", "Carbon", "Nickel", "Caesium", "Americium", "Rutherfordium"]
    A = [1, 12, 58, 133, 243, 261]
    IP = [13.59843449, 11.2602880, 7.639878, 3.893905695, 5.97381, 6.02]
    for k, idx in enumerate(idxs):
        assert ELEMENT_Z[idx]    == Z[k]
        assert ELEMENT_ES[idx]   == ES[k]
        assert ELEMENT_NAME[idx] == NAME[k]
        assert ELEMENT_A[idx]    == A[k]
        assert ELEMENT_IP[idx]   == pytest.approx(IP[k])

def test_reference():
    #Full test
    for i, row in enumerate(_REFTABLE):
        assert ELEMENT_IP[i] == pytest.approx(row[4])
        assert (ELEMENT_Z[i], ELEMENT_ES[i], ELEMENT_NAME[i], ELEMENT_A[i]) == row[:-1]

# Reference table copied from resource files on 2020/05/26
_REFTABLE = [
    (1, "H", "Hydrogen", 1, 13.59843449),
    (2, "He", "Helium", 4, 24.58738880),
    (3, "Li", "Lithium", 7, 5.39171495),
    (4, "Be", "Beryllium", 9, 9.322699),
    (5, "B", "Boron", 11, 8.298019),
    (6, "C", "Carbon", 12, 11.2602880),
    (7, "N", "Nitrogen", 14, 14.53413),
    (8, "O", "Oxygen", 16, 13.618055),
    (9, "F", "Fluorine", 19, 17.42282),
    (10, "Ne", "Neon", 20, 21.564540),
    (11, "Na", "Sodium", 23, 5.1390769),
    (12, "Mg", "Magnesium", 24, 7.646236),
    (13, "Al", "Aluminium", 27, 5.985769),
    (14, "Si", "Silicon", 28, 8.15168),
    (15, "P", "Phosphorus", 31, 10.486686),
    (16, "S", "Sulfur", 32, 10.36001),
    (17, "Cl", "Chlorine", 35, 12.967632),
    (18, "Ar", "Argon", 40, 15.7596117),
    (19, "K", "Potassium", 39, 4.34066369),
    (20, "Ca", "Calcium", 40, 6.1131554),
    (21, "Sc", "Scandium", 45, 6.56149),
    (22, "Ti", "Titanium", 48, 6.828120),
    (23, "V", "Vanadium", 51, 6.746187),
    (24, "Cr", "Chromium", 52, 6.76651),
    (25, "Mn", "Manganese", 55, 7.4340379),
    (26, "Fe", "Iron", 56, 7.9024681),
    (27, "Co", "Cobalt", 59, 7.88101),
    (28, "Ni", "Nickel", 58, 7.639878),
    (29, "Cu", "Copper", 63, 7.726380),
    (30, "Zn", "Zinc", 64, 9.394197),
    (31, "Ga", "Gallium", 69, 5.9993020),
    (32, "Ge", "Germanium", 74, 7.899435),
    (33, "As", "Arsenic", 75, 9.78855),
    (34, "Se", "Selenium", 80, 9.752392),
    (35, "Br", "Bromine", 79, 11.81381),
    (36, "Kr", "Krypton", 84, 13.9996053),
    (37, "Rb", "Rubidium", 85, 4.1771280),
    (38, "Sr", "Strontium", 88, 5.69486740),
    (39, "Y", "Yttrium", 89, 6.21726),
    (40, "Zr", "Zirconium", 90, 6.634126),
    (41, "Nb", "Niobium", 93, 6.75885),
    (42, "Mo", "Molybdenum", 98, 7.09243),
    (43, "Tc", "Technetium", 97, 7.11938),
    (44, "Ru", "Ruthenium", 102, 7.36050),
    (45, "Rh", "Rhodium", 103, 7.45890),
    (46, "Pd", "Palladium", 106, 8.336839),
    (47, "Ag", "Silver", 107, 7.576234),
    (48, "Cd", "Cadmium", 114, 8.993820),
    (49, "In", "Indium", 115, 5.7863556),
    (50, "Sn", "Tin", 120, 7.343918),
    (51, "Sb", "Antimony", 121, 8.608389),
    (52, "Te", "Tellurium", 130, 9.009808),
    (53, "I", "Iodine", 127, 10.451260),
    (54, "Xe", "Xenon", 132, 12.1298436),
    (55, "Cs", "Caesium", 133, 3.893905695),
    (56, "Ba", "Barium", 138, 5.2116646),
    (57, "La", "Lanthanum", 139, 5.5769),
    (58, "Ce", "Cerium", 140, 5.5386),
    (59, "Pr", "Praseodymium", 141, 5.4702),
    (60, "Nd", "Neodymium", 142, 5.5250),
    (61, "Pm", "Promethium", 147, 5.58187),
    (62, "Sm", "Samarium", 152, 5.64371),
    (63, "Eu", "Europium", 153, 5.670385),
    (64, "Gd", "Gadolinium", 156, 6.14980),
    (65, "Tb", "Terbium", 159, 5.8638),
    (66, "Dy", "Dysprosium", 164, 5.93905),
    (67, "Ho", "Holmium", 165, 6.0215),
    (68, "Er", "Erbium", 166, 6.1077),
    (69, "Tm", "Thulium", 169, 6.18431),
    (70, "Yb", "Ytterbium", 174, 6.254160),
    (71, "Lu", "Lutetium", 175, 5.425871),
    (72, "Hf", "Hafnium", 180, 6.825070),
    (73, "Ta", "Tantalum", 181, 7.549571),
    (74, "W", "Tungsten", 184, 7.86403),
    (75, "Re", "Rhenium", 187, 7.83352),
    (76, "Os", "Osmium", 192, 8.43823),
    (77, "Ir", "Iridium", 193, 8.96702),
    (78, "Pt", "Platinum", 195, 8.95883),
    (79, "Au", "Gold", 197, 9.225554),
    (80, "Hg", "Mercury", 202, 10.437504),
    (81, "Tl", "Thallium", 205, 6.1082873),
    (82, "Pb", "Lead", 208, 7.4166799),
    (83, "Bi", "Bismuth", 209, 7.285516),
    (84, "Po", "Polonium", 210, 8.418070),
    (85, "At", "Astatine", 210, 9.31751),
    (86, "Rn", "Radon", 222, 10.74850),
    (87, "Fr", "Francium", 223, 4.0727410),
    (88, "Ra", "Radium", 226, 5.2784239),
    (89, "Ac", "Actinium", 227, 5.380226),
    (90, "Th", "Thorium", 232, 6.30670),
    (91, "Pa", "Protactinium", 231, 5.89),
    (92, "U", "Uranium", 238, 6.19405),
    (93, "Np", "Neptunium", 237, 6.26554),
    (94, "Pu", "Plutonium", 244, 6.02576),
    (95, "Am", "Americium", 243, 5.97381),
    (96, "Cm", "Curium", 247, 5.99141),
    (97, "Bk", "Berkelium", 247, 6.19785),
    (98, "Cf", "Californium", 251, 6.28166),
    (99, "Es", "Einsteinium", 254, 6.36758),
    (100, "Fm", "Fermium", 257, 6.50),
    (101, "Md", "Mendelevium", 256, 6.58),
    (102, "No", "Nobelium", 259, 6.62621),
    (103, "Lr", "Lawrencium", 260, 4.96),
    (104, "Rf", "Rutherfordium", 261, 6.02),
    (105, "Db", "Dubnium", 262 ,6.8)
]