class User_Account:
    def __init__ (self,user_id,user_name,password,events,contatct_information):
        self.user_id=user_id
        self.user_name=user_name
        self.password=password
        self.events=events
        self.contact_information=contatct_information
        
        
    def delete_account(self):
        pass
        
    def initiate_event_creation(self):
        pass
        
    def log_out(self):
        pass
        
    def initiate_RSVP(self):
        pass

    def initiate_comment(self):
        pass

    def customize_account(self):
        pass

    def get_username(self):
        return self.user_name

    def set_username(self,user_name):
        self.user_name= user_name

    def get_password(self):
        return self.password

    def set_password(self,password):
        self.password=password
    
    def get_events(self):
        return self.events

    def add_event(self):
        pass
            