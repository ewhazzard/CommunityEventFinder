from Utils.Contact_Info import Contact_Info


class Event_Details:
    def __init__(self, event_title, event_description, event_contact_info, event_date):
        self.__event_title = event_title
        self.__event_description = event_description
        self.__event_contact_info = event_contact_info
        self.__event_date = event_date

    def get_date(self):
        ''' Getter for the date instance variable '''
        return self.__event_date

    def get_description(self):
        ''' Getter for the description instance variable '''
        return self.__event_description

    def get_title(self):
        ''' Getter for the title instance variable '''
        return self.__event_title

    def get_contact_info(self):
        ''' Getter for the contact_info instance variable '''
        return self.__event_contact_info

    def set_title(self, title):
        ''' Setter for the title instance variable '''
        self.__event_title = title

    def set_description(self, desc):
        ''' Setter for the description instance variable '''
        self.__event_description = desc

    def set_location(self, loca):
        ''' Setter for the location instance variable '''
        self.__event_location = loca

    def set_city(self, city):
        ''' Setter for the city instance variable '''
        self.__event_city = city

    def set_date(self, date):
        ''' Setter for the date instance variable '''
        self.__event_date = date
