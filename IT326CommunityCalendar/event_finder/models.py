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
    user_phone = models.IntegerField(verbose_name="Phone Number")
    user_hobbies = models.JSONField(verbose_name="Hobbies")
    user_interests = models.JSONField(verbose_name="Interests")
    user_email = models.CharField(verbose_name="Email", max_length=100)
    user_age = models.IntegerField(verbose_name="Age")
    user_gender = models.CharField(verbose_name="Gender", choices = GENDER_CHOICES, max_length=25)
    user_city = models.CharField(verbose_name="Location: City", max_length=100)
    user_state = models.CharField(verbose_name="Location: State", max_length=100)
    user_admin = models.BooleanField(verbose_name="Is Admin")

class Event(models.Model):

    event_id = models.IntegerField(verbose_name="Event ID", primary_key=True)
    user_id = models.IntegerField(verbose_name="Event ID", foreign_key=True)
    event_name = models.CharField(verbose_name="Event Name", max_length=50)

    
