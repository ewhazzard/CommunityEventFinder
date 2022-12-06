import pytest

from Utils.Location import Location

def test_location_creation():
    testLocation = Location("123 Easy Street", "Chicago", "Illinois", 60123)

    assert testLocation.get_street() == "123 Easy Street"
    assert testLocation.get_city() == "Chicago"
    assert testLocation.get_state() == "Illinois"
    assert testLocation.get_zipcode() == 60123
