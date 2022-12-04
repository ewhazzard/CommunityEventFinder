import pytest

import os
print(os.getcwd())

print(os.getcwd())

from event import Event
from Contact_Info import Contact_Info
from event_details import Event_Details
from Location import Location
import datetime


def test_example():
    assert 1 == 1

def test_example2():
    assert 2 == 2

def test_event_contact_info_creation_retrieval():
    testContact = Contact_Info("Dan","Smith","dsmith@ilstu.edu","318-329-2930",Location("","","",0))
    testEventDetails = Event_Details("Neighborhood Party","Fun Social Event",testContact,datetime.date(2022,5,10))
    testEvent = Event("1111",testEventDetails,"2222")

    assert testEvent.get_event_details().get_contact_info().get_first_name() == testContact.get_first_name()
    assert testEvent.get_event_details().get_contact_info().get_last_name() == testContact.get_last_name()
    assert testEvent.get_event_details().get_contact_info().get_email() == testContact.get_email()
    assert testEvent.get_event_details().get_contact_info().get_phone() == testContact.get_phone()

def test_event_location_info_creation_retrieval():
    testLocation = Location("23 Blackberry St","Normal","IL",61606)
    testContact = Contact_Info("Dan","Smith","dsmith@ilstu.edu","318-329-2930",testLocation)
    testEventDetails = Event_Details("Neighborhood Party","Fun Social Event",testContact,datetime.date(2022,5,10))
    testEvent = Event("1111",testEventDetails,"2222")

    assert testEvent.get_event_details().get_contact_info().get_location().get_street() == testLocation.get_street()
    assert testEvent.get_event_details().get_contact_info().get_location().get_city() == testLocation.get_city()
    assert testEvent.get_event_details().get_contact_info().get_location().get_state() == testLocation.get_state()
    assert testEvent.get_event_details().get_contact_info().get_location().get_zipcode() == testLocation.get_zipcode()

def test_user_details_creation_retrieval():
    

