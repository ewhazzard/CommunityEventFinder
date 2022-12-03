import pytest

import os
print(os.getcwd())

print(os.getcwd())

from event import Event
from Contact_Info import Contact_Info
from event_details import Event_Details


def test_example():
    assert 1 == 1

def test_example2():
    assert 2 == 2

def test_event_contact_info_creation_retrieval():
    testContact = Contact_Info("Dan","Smith","dsmith@ilstu.edu","318-329-2930")

    testEvent = Event("1111",testContact,"2222")
    assert testEvent.get_contact_info().get_first_name() == testContact.get_first_name()
    assert testEvent.get_contact_info().get_last_name() == testContact.get_last_name()
    assert testEvent.get_contact_info().get_email() == testContact.get_email()
    assert testEvent.get_contact_info().get_phone() == testContact.get_phone()

def test_event_location_info_creation_retrieval():
    pass

