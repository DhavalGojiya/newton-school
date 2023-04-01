from .models import Courses
from django import forms
from django.forms import ValidationError


class TeacherCoursesModelForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('course_name', 'standard', 'course_description', 'course_type', 'price')
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'standard': forms.NumberInput(attrs={'class': 'form-control'}),
            'course_description': forms.Textarea(attrs={'class': 'form-control'}),
            'course_type': forms.RadioSelect(),
            'price': forms.NumberInput(attrs={'class': 'form-control'})

        }

    def __init__(self, *args, **kwargs):
        super(TeacherCoursesModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label

    def clean(self):
        cleaned_data = super(TeacherCoursesModelForm, self).clean()
        course_type = cleaned_data.get("course_type")
        price = cleaned_data.get("price")

        if course_type == 'free' and price != 0:
            return self.add_error('price', "Free courses dont have price")

        elif course_type == 'paid' and not price > 0:
            return self.add_error('price', "Paid courses should greater than zero")

        return cleaned_data
