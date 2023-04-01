from .models import CoursePurchases
from django import forms
from django.forms import ValidationError


class StudentEnrollCourseModelForm(forms.ModelForm):
    class Meta:
        model = CoursePurchases
        exclude = ('enroll_time',)

    def __init__(self, *args, **kwargs):
        super(StudentEnrollCourseModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
