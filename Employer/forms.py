from django import forms
from .models import MyUser
from Employer import admin
from django.forms import ModelForm

class UserRegistrationForm(admin.UserCreationForm):
    class Meta:
        model=MyUser
        fields=["email","password1","password2","role"]


class UserSignInForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)