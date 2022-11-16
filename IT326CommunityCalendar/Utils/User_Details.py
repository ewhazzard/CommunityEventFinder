from Location import Location

class User_Details:
    def __init__ (self,hobbies,age,intrests,gender):
        self.hobbies=hobbies
        self.age=age
        self.intrests=intrests
        self.gender=gender
        self.loc=Location("","","",0)
    
    def set_location(self,street,city,state,zipcode):
        self.loc.set_street(street)
        self.loc.set_city(city)
        self.loc.set_state(state)
        self.loc.set_zip(zipcode)

    def get_location(self):
        location=self.loc.get_street()+" "+ self.loc.get_city()+" "+self.loc.get_state()+" "+self.loc.get_zip()
        return location
    
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