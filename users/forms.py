from django import forms
from django.forms import ValidationError
from .models import SchoolUser
from django.contrib.auth.forms import PasswordChangeForm
from re import search as reg
from django.contrib.auth import authenticate


class SchoolUserModelForm(forms.ModelForm):
    confirm_password = forms.CharField(required=False, label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}), error_messages={'required': "please confirm your password."})

    class Meta:
        model = SchoolUser
        fields = ['first_name', 'last_name', 'username', 'user_icon', 'email', 'birthdate', 'phone', 'standard',
                  'subject', 'password', 'terms_conditions']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'user_icon': forms.FileInput(attrs={}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(attrs={}),
            'phone': forms.NumberInput(attrs={}),
            'standard': forms.NumberInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'local_address': forms.Textarea(attrs={'cols': 30, 'rows': 2}),
            'permanent_address': forms.Textarea(attrs={'cols': 30, 'rows': 2}),
            'terms_conditions': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

        }
        error_messages = {
            'username': {
                'required': "your username is necessary.",
            },
            'password': {
                'required': "please enter the password.",
            },
            'email': {
                'required': 'your email must needed for communication'
            }
        }

    def clean(self):
        cleaned_data = super(SchoolUserModelForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError(
                "password and confirm_password do not match."
            )
        return cleaned_data

    def clean_email(self):
        val_email = self.cleaned_data.get('email')
        return val_email.lower()

    def clean_password(self):
        val_password = self.cleaned_data.get('password')
        if len(val_password) < 8:
            raise ValidationError(
                "Your Password must contain at least 8 characters."
            )
        elif reg(r'\d+', val_password) and reg(r'[a-z]+', val_password) and reg(r'[A-Z]+', val_password) and \
                reg(r'\W+', val_password) and not reg(r'\s+', val_password):
            return val_password
        else:
            raise ValidationError(
                "your password should contain [A-Z], [a-z], [0-9] and one special keyword characters.")

    def clean_terms_conditions(self):
        val_tc = self.cleaned_data.get('terms_conditions')
        if not val_tc:
            raise ValidationError(
                "You Need to Accept our terms and Agreements"
            )
        return val_tc

    def __init__(self, *args, **kwargs):
        super(SchoolUserModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label


# Login Validation Form
class SchoolUserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               error_messages={'required': "Your username required."})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               error_messages={'required': "Your Password required."}, )

    def clean_username(self):
        val_username = self.cleaned_data['username']
        if not SchoolUser.objects.filter(username=val_username).exists():
            raise ValidationError(f'Username "{val_username}" is not found in our records.')
        return val_username

    def clean(self):
        val_username = self.cleaned_data.get('username')
        val_password = self.cleaned_data.get('password')
        user = authenticate(username=val_username, password=val_password)
        print("M USER", user)
        if user is not None:
            return user
        if val_username:
            self.add_error('password', "You entered incorrect password.")


class FormChangePassword(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        for field in ('old_password', 'new_password1', 'new_password2'):
            self.fields[field].widget.attrs = {'class': 'form-control'}
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label


class SchoolUserEditForm(SchoolUserModelForm):
    class Meta:
        model = SchoolUser
        fields = ['first_name', 'last_name', 'username', 'user_icon', 'email', 'phone', 'local_address', ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'user_icon': forms.FileInput(attrs={'class': 'user-icon', }),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'local_address': forms.Textarea(attrs={'class': 'form-control', 'cols': 10, 'rows': 2}),

        }

    def clean(self):
        cleaned_data = super(SchoolUserModelForm, self).clean()
        return cleaned_data
