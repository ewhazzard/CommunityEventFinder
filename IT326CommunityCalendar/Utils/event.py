from RSVP import RSVP
from comment import Comment
from event_details import Event_Details
from Location import Location
from Contact_Info import Contact_Info


class Event:
    def __init__(self, event_id, event_details, user_id):
        self.__event_id = event_id
        self.__event_details = event_details
        self.__user_id = user_id
        self.comments = []
        self.RSVPs = []

    # def view_details(self,):
    #     pass
    def view_details(self):
        detailsMessage = F"Name: {Event_Details.get_title}" + "\t" + \
            F"Date: {Event_Details.get_date}" + "\n\t" + \
            F"City: {Event_Details.get_city}" + "\n\t" + \
            F"Location: {Event_Details.get_location}" + "\n\n" + \
            F"Description: {Event_Details.get_description}" + "\n\n"
        return detailsMessage

    def get_event_details(self):
        return self.__event_details
        
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
