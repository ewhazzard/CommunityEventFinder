from IT326CommunityCalendar.Utils.User_Details import User_Details


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

    # Constructor
    def __init__(self, user_id, user_name, password):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password

    # Not sure we need this functionality here. Probably should be handled purely in the Django class
    def delete_account(self):
        pass
    # Function to start a list of Event objects the user has created

    def initiate_event_creation(self):
        pass
    # Not sure we need this functionality here. Probably should be handled purely in the Django class

    def log_out(self):
        pass

    def initiate_RSVP(self):
        pass

    def initiate_comment(self):
        pass
    # Pass in the age, gender, interests, and hobbies for a user
    # and create a User_Details object with that information

    def customize_account(self, age, gender, interests, hobbies):
        self.user_details = User_Details(age, gender, interests, hobbies)

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

    def add_event(self):
        pass
