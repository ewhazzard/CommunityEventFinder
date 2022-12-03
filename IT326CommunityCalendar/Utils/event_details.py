class Event_Details:
    def __init__(self, event_title, event_description, event_location, event_city, event_date):
        self.__event_title = event_title
        self.__event_description = event_description
        self.__event_location = event_location
        self.__event_city = event_city
        self.__event_date = event_date

    def get_date(self):
        return self.__event_date

    def get_description(self):
        return self.__event_description

    def get_city(self):
        return self.__event_city

    def get_title(self):
        return self.__event_title

    def get_location(self):
        return self.__event_location

    def set_title(self, title):
        self.__event_title = title

    def set_description(self, desc):
        self.__event_description = desc

    def set_location(self, loca):
        self.__event_location = loca

    def set_city(self, city):
        self.__event_city = city

    def create_contact_info():
        pass
