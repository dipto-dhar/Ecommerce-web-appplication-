from django import forms
from ecom_admin.models import User
from django.contrib.auth.models import Group
from .models import *
from django.contrib.auth.forms import UserCreationForm
from tinymce.widgets import TinyMCE


class register_user(UserCreationForm):


    name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter full name'}))
    # username=forms.CharField( label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a username'}))
    email=forms.EmailField( label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a valid email'}))
    phone=forms.IntegerField(label='',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter a valid phone number'}))
    password1=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

    date_joined=forms.TimeField(required=False)

    class Meta:
        model=User
        fields=('name','email','phone','password1','password2')

