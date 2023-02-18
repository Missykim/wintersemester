from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    given_name = 'Melissa'
    family_name = 'Judd'
    full_name = make_full_name(given_name, family_name)
    assert full_name == 'Judd;Melissa'


def test_extract_family_name():
    full_name='Judd;Melissa'
    family_name = extract_family_name(full_name)
    assert family_name == 'Judd'


def test_extract_given_name():
    full_name='Judd;Melissa'
    given_name = extract_given_name(full_name)
    assert given_name == "Melissa"


pytest.main(["-v", "--tb=line", "-rN", __file__])
