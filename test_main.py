import pytest

from main import filter_heroes

def test_filter_heroes_gender():
    assert filter_heroes("male", True)["appearance"]["gender"] == "Male"
    assert filter_heroes("Male", True)["appearance"]["gender"] == "Male"
    assert filter_heroes("mALE", True)["appearance"]["gender"] == "Male"
    assert filter_heroes("MALE", True)["appearance"]["gender"] == "Male"

    assert filter_heroes("female", True)["appearance"]["gender"] == "Female"
    assert filter_heroes("Female", True)["appearance"]["gender"] == "Female"
    assert filter_heroes("fEMALE", True)["appearance"]["gender"] == "Female"
    assert filter_heroes("FEMALE", True)["appearance"]["gender"] == "Female"

    assert filter_heroes("qwerty", True) == None

def test_filter_heroes_work():
    hero_employed = filter_heroes("male", True)
    assert hero_employed["work"]["occupation"] != "-"

    hero_unemployed = filter_heroes("male", False)
    assert hero_unemployed["work"]["occupation"] == "-"

def test_filter_heroes_returns_tallest_male():
    tallest_man = filter_heroes("male", True)
    height = tallest_man["appearance"]["height"][1]
    assert height == "15.2 meters"

def test_filter_heroes_returns_tallest_female():
    tallest_man = filter_heroes("female", True)
    height = tallest_man["appearance"]["height"][1]
    assert height == "62.5 meters"

def test_filter_heroes_incorrect_gender_int():
    with pytest.raises(TypeError):
        filter_heroes(123, True)

def test_filter_heroes_incorrect_work():
    with pytest.raises(TypeError):
        filter_heroes("female", 1)