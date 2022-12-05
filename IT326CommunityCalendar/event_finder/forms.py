from django import forms
from django.forms import ModelForm, widgets
from .models import Users, Event, Comment, RSVP

class CEFForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
        widgets = {
            'gender': widgets.RadioSelect()
        }
        
class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['user_username', 'user_password']


class CreateEvent(ModelForm):
     class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'event_date': widgets.SelectDateWidget()
        }

class EditEvent(ModelForm):
     class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'event_date': widgets.SelectDateWidget()
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        
class RSVPForm(ModelForm):
    class Meta:
        model = RSVP
        fields = '__all__'