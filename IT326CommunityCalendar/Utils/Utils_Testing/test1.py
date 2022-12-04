import pytest

from Utils.event import Event
from Utils.Contact_Info import Contact_Info
from Utils.event_details import Event_Details
from Utils.Location import Location
from Utils.User_Details import User_Details
from Utils.User_Account import User_Account
import datetime



def test_event_details_creation_retrieval():
    testEventDetails = Event_Details("Neighborhood Party","Fun Social Event",Contact_Info("","","","",Location("","","",0)),datetime.date(2022,5,10))
    testEvent = Event("1111","2222",testEventDetails)

    assert testEvent.get_event_details().get_date() == testEventDetails.get_date()
    assert testEvent.get_event_details().get_description() == testEventDetails.get_description()
    assert testEvent.get_event_details().get_title() == testEventDetails.get_title()


def test_event_contact_info_creation_retrieval():
    testContact = Contact_Info("Dan","Smith","dsmith@ilstu.edu","318-329-2930",Location("","","",0))
    testEventDetails = Event_Details("Neighborhood Party","Fun Social Event",testContact,datetime.date(2022,5,10))
    testEvent = Event("1111","2222",testEventDetails)

    assert testEvent.get_event_details().get_contact_info().get_first_name() == testContact.get_first_name()
    assert testEvent.get_event_details().get_contact_info().get_last_name() == testContact.get_last_name()
    assert testEvent.get_event_details().get_contact_info().get_email() == testContact.get_email()
    assert testEvent.get_event_details().get_contact_info().get_phone() == testContact.get_phone()

def test_event_location_info_creation_retrieval():
    testLocation = Location("23 Blackberry St","Normal","IL",61606)
    testContact = Contact_Info("Dan","Smith","dsmith@ilstu.edu","318-329-2930",testLocation)
    testEventDetails = Event_Details("Neighborhood Party","Fun Social Event",testContact,datetime.date(2022,5,10))
    testEvent = Event("1111","2222",testEventDetails)

    assert testEvent.get_event_details().get_contact_info().get_location().get_street() == testLocation.get_street()
    assert testEvent.get_event_details().get_contact_info().get_location().get_city() == testLocation.get_city()
    assert testEvent.get_event_details().get_contact_info().get_location().get_state() == testLocation.get_state()
    assert testEvent.get_event_details().get_contact_info().get_location().get_zipcode() == testLocation.get_zipcode()

def test_user_details_creation_retrieval():
    testUserDetails = User_Details(["Fishing","Investing","Computer Programming"],["Religious Events","Computing Conventions"],21,"Male")
    testUserAccount = User_Account(1111,"dsmith123","password$",testUserDetails)

    assert testUserAccount.get_user_details().get_hobbies() == testUserDetails.get_hobbies()
    assert testUserAccount.get_user_details().get_age() == testUserDetails.get_age()
    assert testUserAccount.get_user_details().get_gender() == testUserDetails.get_gender()
    assert testUserAccount.get_user_details().get_intrests() == testUserDetails.get_intrests()



