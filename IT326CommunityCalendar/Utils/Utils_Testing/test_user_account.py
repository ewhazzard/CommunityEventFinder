import pytest

from Utils.User_Account import User_Account
from Utils.Contact_Info import Contact_Info
from Utils.User_Details import User_Details
from Utils.Location import Location
from Utils.event import Event
import datetime

def test_user_details_creation():
    testUserDetails = User_Details(["Soccer","Golf","Running","Swimming"],["Computer Science","Math","Physics"],19,"Boy")

    assert testUserDetails.get_age() == 19
    assert testUserDetails.get_gender == "Boy"
    assert testUserDetails.get_hobbies==["Soccer","Golf","Running","Swimming"]
    assert testUserDetails.get_intrests==["Computer Science","Math","Physics"]
    