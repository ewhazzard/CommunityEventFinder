import pytest

from Utils.event import Event
from Utils.Contact_Info import Contact_Info
from Utils.event_details import Event_Details
from Utils.Location import Location
from Utils.User_Details import User_Details
from Utils.User_Account import User_Account
import datetime


def test_event_details_creation_retrieval():
    """Testing for 3.1.6- create an event"""
    testEventDetails = Event_Details("Neighborhood Party", "Fun Social Event", Contact_Info(
        "", "", "", "", Location("", "", "", 0)), datetime.date(2022, 5, 10))
    testEvent = Event("1111", "2222", testEventDetails)

    assert testEvent.get_event_details().get_date() == testEventDetails.get_date()
    assert testEvent.get_event_details().get_description(
    ) == testEventDetails.get_description()
    assert testEvent.get_event_details().get_title() == testEventDetails.get_title()


def test_event_contact_info_creation_retrieval():
    """Testing for 3.1.16- Link contact info to event post"""
    testContact = Contact_Info(
        "Dan", "Smith", "dsmith@ilstu.edu", "318-329-2930", Location("", "", "", 0))
    testEventDetails = Event_Details(
        "Neighborhood Party", "Fun Social Event", testContact, datetime.date(2022, 5, 10))
    testEvent = Event("1111", "2222", testEventDetails)

    assert testEvent.get_event_details().get_contact_info(
    ).get_first_name() == testContact.get_first_name()
    assert testEvent.get_event_details().get_contact_info(
    ).get_last_name() == testContact.get_last_name()
    assert testEvent.get_event_details().get_contact_info(
    ).get_email() == testContact.get_email()
    assert testEvent.get_event_details().get_contact_info(
    ).get_phone() == testContact.get_phone()


def test_event_location_info_creation_retrieval():
    """Retriving location from an event"""
    testLocation = Location("23 Blackberry St", "Normal", "IL", 61606)
    testContact = Contact_Info(
        "Dan", "Smith", "dsmith@ilstu.edu", "318-329-2930", testLocation)
    testEventDetails = Event_Details(
        "Neighborhood Party", "Fun Social Event", testContact, datetime.date(2022, 5, 10))
    testEvent = Event("1111", "2222", testEventDetails)

    assert testEvent.get_event_details().get_contact_info(
    ).get_location().get_street() == testLocation.get_street()
    assert testEvent.get_event_details().get_contact_info(
    ).get_location().get_city() == testLocation.get_city()
    assert testEvent.get_event_details().get_contact_info(
    ).get_location().get_state() == testLocation.get_state()
    assert testEvent.get_event_details().get_contact_info(
    ).get_location().get_zipcode() == testLocation.get_zipcode()




def test_event_with_city_of_interest():
    """
Testing part of the functionality for requirement 3.1.15 (Search for city of interest). User searches for the city "Chicago".
"""
    location1 = Location("23 Blackberry St", "Normal", "IL", 61606)
    location2 = Location("123 Easy Street", "Chicago", "Illinois", 60123)

    contactInfo1 = Contact_Info(
        "Dan", "Smith", "dsmith@ilstu.edu", "318-329-2930", location1)
    contactInfo2 = Contact_Info(
        "Dan", "Smith", "dsmith@ilstu.edu", "318-329-2930", location2)

    eventDetails1 = Event_Details(
        "Neighborhood Party", "Fun Social Event", contactInfo1, datetime.date(2022, 5, 10))
    eventDetails2 = Event_Details(
        "Gathering", "Casual Event", contactInfo2, datetime.date(2022, 6, 13))

    event1 = Event("1234", "5555", eventDetails1)
    event2 = Event("9992", "1222", eventDetails2)

    list = []

    list.append(event1)
    list.append(event2)

    assert list[0].get_event_details().get_contact_info(
    ).get_location().get_city() != "Chicago"
    assert list[1].get_event_details().get_contact_info(
    ).get_location().get_city() == "Chicago"

def test_editing_event_details():
    """Testing 3.1.7- edit event details"""
    location1 = Location("23 Blackberry St", "Normal", "IL", 61606)
    contactInfo1 = Contact_Info(
        "Dan", "Smith", "dsmith@ilstu.edu", "318-329-2930", location1)
    event_details = Event_Details(
        "Neighborhood Party", "Fun Social Event", contactInfo1, datetime.date(2022, 5, 10))
    test_event=Event( 18, 747, event_details)
    assert(test_event.event_details.get_date==event_details.get_date)
    assert(test_event.event_details.get_description==event_details.get_description)
    assert(test_event.event_details.get_title==event_details.get_title)
    test_event.event_details.set_date(datetime(2022,5,12))
    test_event.event_details.set_description("verry Fun Social Event")
    test_event.event_details.set_title("City Party")
    assert(test_event.event_details.get_date==datetime(2022,5,12))
    assert(test_event.event_details.get_description=="verry Fun Social Event")
    assert(test_event.event_details.get_title=="City Party")

def test_countdown_timer():
    """Testing for 3.1.19- display countdown timer for events"""
    location1 = Location("23 Blackberry St", "Normal", "IL", 61606)
    contactInfo1 = Contact_Info(
        "Dan", "Smith", "dsmith@ilstu.edu", "318-329-2930", location1)
    event_details = Event_Details(
        "Neighborhood Party", "Fun Social Event", contactInfo1, datetime.date(2022, 5, 10))
    test_event=Event( 18, 747, event_details)
    time_diff = str(test_event.event_details.get_date.replace(tzinfo=None) - datetime.now().replace(tzinfo=None))
    assert(time_diff>0)

def test_event_deletion():
    """Tesing for 3.1.12- delete any event"""
    location1 = Location("23 Blackberry St", "Normal", "IL", 61606)
    contactInfo1 = Contact_Info(
        "Dan", "Smith", "dsmith@ilstu.edu", "318-329-2930", location1)
    event_details = Event_Details(
        "Neighborhood Party", "Fun Social Event", contactInfo1, datetime.date(2022, 5, 10))
    test_event=Event( 18, 747, event_details)
    del test_event
    assert(test_event!="Neighborhood Party")