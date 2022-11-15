class User_Contact_Info:
    def __init__(self,street,state,city,phone):
        self.street=street
        self.state=state
        self.city=city
        self.phone=phone

    def get_location(self):
        location=self.street+" "+self.city+" "+self.state
        return location

    def get_city(self):
        return self.city

    def get_phone(self):
        return self.phone

    def set_phone(self,phone):
        self.phone=phone

    def set_state(self,state):
        self.state=state

    def set_street(self,street):
        self.street=street