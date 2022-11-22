from django.db import models

# Create your models here.
class Users(models.Model):

    GENDER_CHOICES = (("1","Male"),
                      ("2", "Female"),
                      ("3", "Other"),
                      ("4", "Decline to Answer"))

    user_id = models.IntegerField(primary_key=True)
    user_username = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_fname = models.CharField(max_length=50)
    user_lname = models.CharField(max_length=50)
    user_phone = models.IntegerChoices(max_length=50)
    user_hobbies = models.JSONField()
    user_interests = models.JSONField()
    user_email = models.CharField(max_length=100)
    user_age = models.IntegerField()
    user_gender = models.Choices(choices = GENDER_CHOICES)
    user_city = models.CharField(max_length=100)
    user_state = models.CharField(max_length=100)
    
    def __init__(self):
        return self.user_username
