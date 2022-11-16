
class User_Details:
    def __init__ (self,hobbies,age,intrests,gender):
        self.hobbies=hobbies
        self.age=age
        self.intrests=intrests
        self.gender=gender
        
    
    def get_hobbies(self):
        return self.hobbies

    def get_age(self):
        return self.age

    def get_intrests(self):
        return self.intrests

    def get_gender(self):
        return self.gender

    def set_hobbies(self,hobbies):
        pass

    def set_age(self,age):
        self.age=age

    def set_intrests(self,intrests):
        self.intrests=intrests

    def set_gender(self,gender):
        self.gender=gender