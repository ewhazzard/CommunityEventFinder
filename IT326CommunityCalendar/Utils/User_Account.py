from Utils.User_Details import User_Details
from Utils.Contact_Info import Contact_Info
from Utils.event import Event
from Utils.event_details import Event_Details

class User_Account:
    # Class variables
    # Integer ID unique to each user
    user_id = 0
    # Unique username string
    username = ''
    # Password that passes strength tests and is stored as a String
    password = ''
    # user_details object to hold information about hobbies, interests, age, and gender
    user_details = None
    # List of Event objects that the user has created
    events = []
    # Contact information object that will contain all contact information for a user
    contact_information = None
    # Boolean flag to indicate if the user is an admin
    is_admin = False

    # Constructor
    def __init__(self, user_id, user_name, password, user_details, is_admin,contact_info):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.user_details = user_details
        self.is_admin = is_admin
        self.contact_info=contact_info
        self.RSVP_count=0

    def __str__(self) -> str:
        return self.user_name

    # Not sure we need this functionality here. Probably should be handled purely in the Django class
    def delete_account(self):
        pass
    # Function to start a list of Event objects the user has created

    def initiate_event_creation(self):
        pass
    # Not sure we need this functionality here. Probably should be handled purely in the Django class

    def log_out(self):
        pass

    def initiate_RSVP(self,event_id):
        
        pass

    def initiate_comment(self,event_id,content):
        pass
    # Pass in the age, gender, interests, and hobbies for a user
    # and create a User_Details object with that information

    def customize_account(self, age, gender, interests, hobbies):
        self.user_details = User_Details(age, gender, interests, hobbies)

    def get_user_details(self):
        return self.user_details

    def get_username(self):
        return self.user_name

    def set_username(self, user_name):
        self.user_name = user_name

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_events(self):
        return self.events

    def add_event(self, event_title, event_description,event_date):
        self.event_details=Event_Details(event_title,event_description,self.contact_info,event_date)
        self.event=Event(8,self.user_id, self.event_details) 
        self.events.append(self.event)
        
    def get_user_id(self):
        return self.user_id