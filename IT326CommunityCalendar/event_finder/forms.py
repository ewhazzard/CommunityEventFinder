from django import forms
from django.forms import ModelForm, widgets
from .models import Users, Event

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