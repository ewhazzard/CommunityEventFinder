class Location:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def get_city(self):
        ''' Getter for the city instance variable '''
        return self.city

    def get_street(self):
        ''' Getter for the street instance variable '''
        return self.street

    def get_state(self):
        ''' Getter for the state instance variable '''
        return self.state

    def get_zipcode(self):
        ''' Getter for the zipcode instance variable '''
        return self.zipcode

    def set_city(self, city):
        ''' Setter for the city instance variable '''
        self.city = city

    def set_state(self, state):
        ''' Setter for the state instance variable '''
        self.state = state

    def set_street(self, street):
        ''' Setter for the street instance variable '''
        self.street = street

    def set_zip(self, zipcode):
        ''' Setter for the zip instance variable '''
        self.zipcode = zipcode
