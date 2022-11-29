from django import forms
from django.forms import ModelForm, widgets
from .models import Users

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


class CreateEvent(forms.Form):
    name = forms.CharField(label="name",max_length=200)