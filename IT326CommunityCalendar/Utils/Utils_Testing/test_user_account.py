import pytest

from Utils.User_Account import User_Account
from Utils.Contact_Info import Contact_Info
from Utils.User_Details import User_Details
from Utils.Location import Location
from Utils.event import Event
from Utils.RSVP import RSVP
import datetime

def test_user_details_creation():
    testUserDetails = User_Details(["Soccer","Golf","Running","Swimming"],["Computer Science","Math","Physics"],19,"Boy")

    assert testUserDetails.get_age() == 19
    assert testUserDetails.get_gender == "Boy"
    assert testUserDetails.get_hobbies==["Soccer","Golf","Running","Swimming"]
    assert testUserDetails.get_intrests==["Computer Science","Math","Physics"]

def test_RSVP_creation():
    testUserDetails = User_Details(["Soccer","Golf","Running","Swimming"],["Computer Science","Math","Physics"],19,"Boy")
    user=User_Account(2223, "John_Smith", "Snake_tooth99", testUserDetails)
    contact_info=Contact_Info("John","Smith","john.smith@gmail.com","854-456-7891","Normal, IL")
    event=Event(42387,contact_info,user.get_user_id)
    main_function=user.initiate_RSVP(42387)
    rsvp_test=RSVP(user.get_user_id,datetime.date.today)
    assert rsvp_test.get_user_id == main_function.get_user_id
    assert rsvp_test.get_RSVP_date == main_function.get_RSVP_date

def test_user_details_creation_retrieval():
    testUserDetails = User_Details(["Fishing","Investing","Computer Programming"],["Religious Events","Computing Conventions"],21,"Male")
    testUserAccount = User_Account(1111,"dsmith123","password$",testUserDetails)

    assert testUserAccount.get_user_details().get_hobbies() == testUserDetails.get_hobbies()
    assert testUserAccount.get_user_details().get_age() == testUserDetails.get_age()
    assert testUserAccount.get_user_details().get_gender() == testUserDetails.get_gender()
    assert testUserAccount.get_user_details().get_interests() == testUserDetails.get_interests()