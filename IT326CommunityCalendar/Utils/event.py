from RSVP import RSVP
from comment import Comment
from event_details import Event_Details

class Event:
    # Instance Variables
    # Integer id unique to each event
    event_id = 0
    # Event Details object to describe the event
    event_details = None
    # Contact info object belonging to the Event
    contact_info = None
    # Id of the user who created the Event object
    user_id = 0
    # List of Comment objects that holds all the comments for the event
    comments = []
    # List of RSVP objects that holds RSVP information for the event
    rsvps = []
    
    # Constructor
    def __init__(self,event_id,contact_info,user_id):
        self.event_id=event_id
        self.contact_info=contact_info
        self.user_id=user_id
        self.comments=[]
        self.rsvps=[]
        
    def get_event_id(self):
        return self.event_id
    
    # Getter to return contact information object
    def get_contact_info(self):
        return self.contact_info
    
    # Getter for the Event Details object
    def get_event_details(self):
        return self.event_details
    
    # Setter for Event Details. Constructs an Event Details object
    def set_event_details(self, title, description, location, city, date):
        self.event_details = Event_Details(title, description, location, city, date)
    
    def get_details(self):
        return self.event_details

    def add_RSVP(self,id):
        pass

    def add_comment(self,id):
        pass

    def remove_RSVP(self,id):
        pass

    def remove_comment(self,id): 
        pass