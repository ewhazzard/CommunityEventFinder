import pytest

from Utils.User_Account import User_Account
from Utils.Contact_Info import Contact_Info
from Utils.User_Details import User_Details
from Utils.Location import Location
from Utils.event import Event
from Utils.RSVP import RSVP
from Utils.comment import Comment
import datetime


def test_user_details_creation():
    
    """Testing part of the functionality for requirement 3.1.1 (Create an account)"""
    testUserDetails = User_Details(["Soccer", "Golf", "Running", "Swimming"], [
                                   "Computer Science", "Math", "Physics"], 19, "Boy")

    assert testUserDetails.get_age() == 19
    assert testUserDetails.get_gender() == "Boy"
    assert testUserDetails.get_hobbies() == [
        "Soccer", "Golf", "Running", "Swimming"]
    assert testUserDetails.get_interests() == [
        "Computer Science", "Math", "Physics"]


def test_RSVP_creation():

    """Testing part of the functionality for requirement 3.1.8 (RSVP to an event)"""

    testUserDetails = User_Details(["Soccer", "Golf", "Running", "Swimming"], [
                                   "Computer Science", "Math", "Physics"], 19, "Boy")
    contact_info = Contact_Info(
        "John", "Smith", "john.smith@gmail.com", "854-456-7891", "Normal, IL")
    user = User_Account(2223, "John_Smith", "Snake_tooth99", testUserDetails,False,contact_info)
    event = Event(42387, contact_info, user.get_user_id())
    main_function = user.initiate_RSVP(42387)
    rsvp_test = RSVP(datetime.date.today(), user.get_user_id())
    assert rsvp_test.get_user_id() == main_function.get_user_id()
    assert rsvp_test.get_RSVP_date() == main_function.get_RSVP_date()


def test_user_details_creation_retrieval():
    testUserDetails = User_Details(["Fishing", "Investing", "Computer Programming"], [
                                   "Religious Events", "Computing Conventions"], 21, "Male")
    testUserAccount = User_Account(
        1111, "dsmith123", "password$", testUserDetails,False,Contact_Info("John","Smith","john.smith@gmail.com","356-455-9239", Location("","","","")))

    assert testUserAccount.get_user_details(
    ).get_hobbies() == testUserDetails.get_hobbies()
    assert testUserAccount.get_user_details().get_age() == testUserDetails.get_age()
    assert testUserAccount.get_user_details(
    ).get_gender() == testUserDetails.get_gender()
    assert testUserAccount.get_user_details(
    ).get_interests() == testUserDetails.get_interests()


def test_comment_creation():

    """Testing part of the functionality for requirement 3.1.10 (Comment on event posting)"""
    testUserDetails = User_Details(["Fishing", "Investing", "Computer Programming"], [
                                   "Religious Events", "Computing Conventions"], 21, "Male")
    user = User_Account(2223, "John_Smith", "Snake_tooth99", testUserDetails,False,Contact_Info("John","Smith","john.smith@gmail.com","356-455-9239", Location("","","","")))
    contact_info = Contact_Info(
        "John", "Smith", "john.smith@gmail.com", "854-456-7891", "Normal, IL")
    event = Event(42387, contact_info, user.get_user_id())
    main_function = user.initiate_comment(42387, "this is the comment")
    test_comment = Comment("this is the comment", 1,
                           datetime.date.today(), user.get_user_id())
    assert test_comment.get_content() == main_function.get_content()
    assert test_comment.get_date() == main_function.get_date()
