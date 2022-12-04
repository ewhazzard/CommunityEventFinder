from Utils.RSVP import RSVP
from Utils.comment import Comment
from Utils.event_details import Event_Details
from Utils.Location import Location
from Utils.Contact_Info import Contact_Info


class Event:
    # Instance Variables
    # Integer id unique to each event
    event_id = 0
    # Event Details object to describe the event
    event_details = None
    # Id of the user who created the Event object
    user_id = 0
    # List of Comment objects that holds all the comments for the event
    comments = []
    # List of RSVP objects that holds RSVP information for the event
    rsvps = []
    
    def __init__(self,event_id,user_id, event_details):
        self.event_id=event_id
        self.user_id=user_id
        self.comments=[]
        self.rsvps=[]
        self.event_details = event_details
    
    def view_details(self):
        detailsMessage = F"Name: {Event_Details.get_title}" + "\t" + \
            F"Date: {Event_Details.get_date}" + "\n\t" + \
            F"City: {Event_Details.get_city}" + "\n\t" + \
            F"Location: {Event_Details.get_location}" + "\n\n" + \
            F"Description: {Event_Details.get_description}" + "\n\n"
        return detailsMessage

    def get_event_details(self):
        return self.event_details
    
    # Setter for Event Details. Constructs an Event Details object
    def set_event_details(self, title, description, location, city, date):
        self.event_details = Event_Details(title, description, location, city, date)
        
    def add_RSVP(self, id):
        rsvp = RSVP(RSVP.get_RSVP_date, RSVP.get_user_id)

    def add_comment(self, id, message):
        # def __init__(self, content, comment_id, comment_date, user_id):
        # Create new Comment object ?
        # What should comment_id and user_id be?
        c = Comment(message, Comment.get_date, 0)
        c.set_content(message)

    def remove_RSVP(self, id):
        pass
        # Remove same RSVP object

    def remove_comment(self, id):
        pass
        # Remove same Comment object

    def create_event_details(self, event_id, user_id, comments, event_details, rsvps):
        # Needs locaiton, contactInfo, and eventDetails
        loc = Location.get_city + "\n" + Location.get_street + \
            "\n" + Location.get_city + "\n" + Location.get_zipcode

        contactInfo = Contact_Info.get_first_name + " " + Contact_Info.get_last_name + "\n" + \
            Contact_Info.get_email + "\n" + Contact_Info.get_location + \
            "\n" + Contact_Info.get_phone

        eventDetails = Event.view_details(self)

        event_details_obj = Event_Details(
            loc, contactInfo, eventDetails)

        # Return it?
        # return event_details_obj
