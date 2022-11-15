from RSVP import RSVP
from comment import Comment
from event_details import Event_Details

class Event:
    def __init__(self,event_id,contact_info,user_id):
        self.__event_id=event_id
        self.__contact_info=contact_info
        self.__user_id=user_id
        self.comments=[]
        self.RSVPs=[]
    
    def view_details(self,):
        pass

    def add_RSVP(self,id):
        pass

    def add_comment(self,id):
        pass

    def remove_RSVP(self,id):
        pass

    def remove_comment(self,id): 
        pass