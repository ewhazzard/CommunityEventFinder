class User_Details:

    def __init__(self, hobbies, intrests, age, gender):
        """ Class constructor. """
        self.hobbies = hobbies
        self.intrests = intrests
        self.age = age
        self.gender = gender

    def get_hobbies(self):
        """ Getter for the hobbies variable. """
        return self.hobbies

    def get_age(self):
        """ Getter for the age variable. """
        return self.age

    def get_interests(self):
        """ Getter for the interests variable. """
        return self.intrests

    def get_gender(self):
        """ Getter for the gender variable. """
        return self.gender

    def add_hobbies(self, hobbies_to_add):
        """ Adds elements to the hobbies list. """
        self.hobbies.extend(hobbies_to_add)

    def set_age(self, age):
        """ Setter for the age variable. """
        self.age = age

    def set_intrests(self, intrests):
        """ Setter for the interests variable. """
        self.intrests = intrests

    def set_gender(self, gender):
        """ Setter for the gender variable. """
        self.gender = gender
