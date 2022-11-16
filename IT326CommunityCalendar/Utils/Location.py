class Location:
    def __init__(self,street,city,state,zipcode):
        self.street=street
        self.city=city
        self.state=state
        self.zipcode=zipcode

    def get_city(self):
        return self.city

    def get_street(self):
        return self.street

    def get_state(self):
        return self.state

    def get_zipcode(self):
        return self.zipcode

    def set_city(self,city):
        self.city=city

    def set_state(self,state):
        self.state=state

    def set_street(self,street):
        self.street=street

    def set_zip(self,zipcode):
        self.zipcode=zipcode