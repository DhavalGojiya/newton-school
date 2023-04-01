from django import forms
from .models import School


class SchoolModelForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['established_year', 'rating', 'address', 'owner_name']
        error_messages = {
            'owner_name': {'required': "Please Enter Correct Name"}
        }
