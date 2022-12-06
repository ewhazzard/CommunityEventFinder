from Utils.User_Details import User_Details
from Utils.Contact_Info import Contact_Info
from Utils.event import Event
from Utils.event_details import Event_Details
from Utils.RSVP import RSVP
from Utils.comment import Comment
from datetime import date

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
        """returns the user name"""
        return self.user_name

    def delete_account(self):
        """deletes account"""
        pass

    def initiate_event_creation(self,event):
        """saves event to event list"""
        event1=event
        self.events.append(event1)

    def log_out(self):
        """user logs out"""
        pass

    def initiate_RSVP(self,event_id):
        """user RSVPs to an event"""
        creationRSVP = RSVP(date.today(),self.user_id)
        return creationRSVP

    def initiate_comment(self,event_id,content):
        """user makes a comment on an event"""
        creationComment = Comment(content,1,date.today(), self.user_id)
        return creationComment

    def customize_account(self, age, gender, interests, hobbies):
        """ Pass in the age, gender, interests, and hobbies for a user
     and create a User_Details object with that information"""
        self.user_details = User_Details(age, gender, interests, hobbies)

    def get_user_details(self):
        """returns user details"""
        return self.user_details
    
    def get_username(self):
        """returns username"""
        return self.user_name
    
    def set_username(self, user_name):
        """changes value of user name"""
        self.user_name = user_name
    
    def get_password(self):
        '''returns users password'''
        return self.password

    def set_password(self, password):
        """changes value of users password"""
        self.password = password

    def get_events(self):
        """returns list of events the user made"""
        return self.events

    def add_event(self, event_title, event_description,event_date):
        """user creates an event and adds it to the list of events"""
        self.event_details=Event_Details(event_title,event_description,self.contact_info,event_date)
        self.event=Event(8,self.user_id, self.event_details) 
        self.initiate_event_creation(self.event)
        
    def get_user_id(self):
        """return the users id"""
        return self.user_id