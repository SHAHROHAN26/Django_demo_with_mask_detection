from django import forms
from django.contrib.auth.models import User
from app1.models import Login_table
from django.core import validators
from django.core.validators import RegexValidator

class UserForm(forms.ModelForm):
    user = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = Login_table
        fields = ('user','password')
