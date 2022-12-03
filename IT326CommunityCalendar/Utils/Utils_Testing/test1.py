import pytest

from event import Event
from Contact_Info import Contact_Info
from event_details import Event_Details


def test_example():
    assert 1 == 1

def test_example2():
    assert 2 == 2

def test_event_location_creation_retrieval():
    testContact = Contact_Info("Dan","Smith","dsmith@ilstu.edu","318-329-2930")

    testEvent = Event("1111",testContact,"2222")
    assert testEvent.get_contact_info().get_first_name() == testContact.get_first_name()
