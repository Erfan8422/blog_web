from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
        error_messages = {
            'username': {
                'unique': "This username is already exist"
            },

            'password1': {
                'min_length': "ز"
            },

            'password2': {
                'password_mismatch': "Two passwords are not match",
                'numeric': "Password should not be all numeric",
                'alphabetic': "Password should not be all alphabetic"
            },

            'email': {
                'unique': "This email is already exist"
            }
        }


    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        password1 = self.cleaned_data.get('password1')
        if password2.isnumeric() or password2.isalpha():
            raise forms.ValidationError("Password should not be all numeric or all alphabetic")
        if password2 != password1:
            raise forms.ValidationError("Two passwords are not match")
        if len(password1) < 8:
            raise forms.ValidationError("This password is too short.It must be atleast 8 characters")
        return password2


