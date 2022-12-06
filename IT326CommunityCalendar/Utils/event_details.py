from Utils.Contact_Info import Contact_Info


class Event_Details:
    def __init__(self, event_title, event_description, event_contact_info, event_date):
        self.__event_title = event_title
        self.__event_description = event_description
        self.__event_contact_info = event_contact_info
        self.__event_date = event_date

    ''' Getter for the date instance variable '''

    def get_date(self):
        return self.__event_date

    ''' Getter for the description instance variable '''

    def get_description(self):
        return self.__event_description

    ''' Getter for the title instance variable '''

    def get_title(self):
        return self.__event_title

    ''' Getter for the contact_info instance variable '''

    def get_contact_info(self):
        return self.__event_contact_info

    ''' Setter for the title instance variable '''

    def set_title(self, title):
        self.__event_title = title

    ''' Setter for the description instance variable '''

    def set_description(self, desc):
        self.__event_description = desc

    ''' Setter for the location instance variable '''

    def set_location(self, loca):
        self.__event_location = loca

    ''' Setter for the city instance variable '''

    def set_city(self, city):
        self.__event_city = city

    ''' Setter for the date instance variable '''

    def set_date(self, date):
        self.__event_date = date
