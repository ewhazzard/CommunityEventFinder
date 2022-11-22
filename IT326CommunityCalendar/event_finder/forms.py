from django.forms import ModelForm, widgets
from .models import Users

class CEFForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
        widgets = {
            'gender': widgets.RadioSelect()
        }