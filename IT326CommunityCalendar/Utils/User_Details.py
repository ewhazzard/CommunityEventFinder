class User_Details:

    # List of strings. Each element is a hobby
    hobbies = []
    # List of strings. Each element is an interest
    interests = []
    # Integer age of the user
    age = 0
    # String representation of Gender
    gender = ''

    def __init__(self, hobbies, intrests, age, gender):
        self.hobbies = hobbies
        self.intrests = intrests
        self.age = age
        self.gender = gender

    def get_hobbies(self):
        return self.hobbies

    def get_age(self):
        return self.age

    def get_intrests(self):
        return self.intrests

    def get_gender(self):
        return self.gender

    def add_hobbies(self, hobbies_to_add):
        self.hobbies.extend(hobbies_to_add)

    def set_age(self, age):
        self.age = age

    def set_intrests(self, intrests):
        self.intrests = intrests

    def set_gender(self, gender):
        self.gender = gender
