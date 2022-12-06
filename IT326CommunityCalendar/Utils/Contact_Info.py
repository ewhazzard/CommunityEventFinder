from Utils.Location import Location

class Contact_Info:

    
    def __init__(self,first_name,last_name,email,phone,location):
        """ Class constructor. """
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone=phone
        self.location = location
    
    def set_location(self,street,city,state,zipcode):
        """ Setter for the location variable. """
        self.loc.set_street(street)
        self.loc.set_city(city)
        self.loc.set_state(state)
        self.loc.set_zip(zipcode)

    def get_location(self):
        """ Getter for the location variable. """
        return self.location

    def get_first_name(self):
        """ Getter for the first name variable. """
        return self.first_name

    def get_phone(self):
        """ Getter for the phone variable."""
        return self.phone

    def set_phone(self,phone):
        """ Setter for the phone variable. """
        self.phone=phone

    def get_last_name(self):
        """ Getter for the last name variable. """
        return self.last_name

    def get_email(self):
        """ Getter for the email variable. """
        return self.email

    def set_phone(self,phone):
        """ Setter for the phone variable. """
        self.phone=phone

    def set_first_name(self,first_name):
        """ Setter for the first name variable. """
        self.first_name=first_name

    def set_last_name(self,last_name):
        """ Setter for the last name variable. """
        self.last_name=last_name

    def set_email(self,email):
        """ Setter for the email variable. """
        self.email=email