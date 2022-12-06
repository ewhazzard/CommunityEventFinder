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
        # fields = ['user_id','event_title','event_description',
        #         'event_date','creator_first_name','creator_last_name','event_email',
        #         'event_phone','event_city','event_state', 'event_flagged']
        fields = '__all__'
        widgets = {
            'event_date': widgets.SelectDateWidget()
        }

class EditProfile(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        
class RSVPForm(ModelForm):
    class Meta:
        model = RSVP
        fields = '__all__'

class SearchForm(ModelForm):
    event_title = forms.CharField(required=False)
    event_city = forms.CharField(required=False)
    event_state = forms.CharField(required=False)
    class Meta:
        model = Event
        fields = ['event_title','event_city','event_state']
        