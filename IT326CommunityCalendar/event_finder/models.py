from django.db import models

# Create your models here.
# User model to hold the account information for Community Event Finder
# TODO: Make aggregate columns that hold Location and Contact objects
class Users(models.Model):

    GENDER_CHOICES = (("1","Male"),
                      ("2", "Female"),
                      ("3", "Other"),
                      ("4", "Decline to Answer"))

    user_id = models.IntegerField(verbose_name="User ID", primary_key=True)
    user_username = models.CharField(verbose_name="Username", max_length=50)
    user_password = models.CharField(verbose_name="Password", max_length=50)
    user_fname = models.CharField(verbose_name="First Namen", max_length=50)
    user_lname = models.CharField(verbose_name="Last Name", max_length=50)
    user_phone = models.CharField(verbose_name="Phone Number", max_length=25)
    user_hobbies = models.JSONField(verbose_name="Hobbies")
    user_interests = models.JSONField(verbose_name="Interests")
    user_email = models.CharField(verbose_name="Email", max_length=100)
    user_age = models.IntegerField(verbose_name="Age")
    user_gender = models.CharField(verbose_name="Gender", choices = GENDER_CHOICES, max_length=25)
    user_city = models.CharField(verbose_name="Location: City", max_length=100)
    user_state = models.CharField(verbose_name="Location: State", max_length=100)
    user_street = models.CharField(verbose_name="Location: Street", max_length=100)
    user_zipcode = models.IntegerField(verbose_name="Location: Zipcode")
    user_admin = models.BooleanField(verbose_name="Is Admin")
    
    def __str__(self):
        return self.user_username
  

class Event(models.Model):  
    event_id = models.IntegerField(verbose_name="Event ID", primary_key=True)
    user_id = models.ForeignKey(Users, on_delete = models.CASCADE, verbose_name="OrganizerID")
    event_title = models.CharField(verbose_name="Event Title", max_length=50)
    event_description = models.CharField(verbose_name="Event Description",max_length=256)
    event_date = models.DateTimeField(verbose_name="Event Date")
    creator_first_name = models.CharField(verbose_name="Event Creator First Name",max_length=30)
    creator_last_name = models.CharField(verbose_name="Event Creator Last Name",max_length=30)
    event_email = models.CharField(verbose_name="Event Email", max_length=100)
    event_phone = models.CharField(verbose_name="Event Phone Number", max_length=25)
    event_city = models.CharField(verbose_name="Event Location: City", max_length=100)
    event_state = models.CharField(verbose_name="Event Location: State", max_length=100)
    event_flagged = models.BooleanField(verbose_name="Flagged for Abuse")
    
    def __str__(self):
        return self.event_title

class Comment(models.Model):
    comment_id = models.IntegerField(verbose_name="Comment ID", primary_key=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Event ID")
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="User ID")
    comment_string = models.TextField(verbose_name="Comment")

class RSVP(models.Model):
    rsvp_id = models.IntegerField(verbose_name="RSVP ID",primary_key=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Event ID")
    rsvp_date = models.DateField(verbose_name="RSVP Date")
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Event ID")


    
    

    
