from django import forms
from ecom_admin.models import User
from django.contrib.auth.models import Group
from .models import *
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from tinymce.widgets import TinyMCE


class update_password(SetPasswordForm):
    new_password1=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password'}))
    new_password2=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))
    class Meta:
        model=User
        fields=('new_password1','new_password2')

class register_user(UserCreationForm):
    first_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first name'}))
    last_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last name'}))
    email=forms.EmailField( label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a valid email'}))
    phone=forms.IntegerField(label='',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter a valid phone number'}))
    password1=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))

    class Meta:
        model=User
        fields=('first_name','last_name','email','phone','password1','password2')

class update_user(UserChangeForm):

    password=None
    first_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first name'}))
    last_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last name'}))
    email=forms.EmailField( label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a valid email'}))
    phone=forms.IntegerField(label='',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter a valid phone number'}))

    class Meta:
        model=User
        fields=('first_name','last_name','email','phone')

class shipping_info(forms.ModelForm):

  
    name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter full name'}))
    phone=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter phone number'}))
    email=forms.EmailField( label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a valid email'}))
    country=forms.CharField( label='',widget=forms.Select(attrs={'class':'form-control','id':'country','placeholder':'Enter state'}))
    state=forms.CharField( label='',widget=forms.Select(attrs={'class':'form-control','id':'state','placeholder':'Enter state'}))
    city=forms.CharField( label='',widget=forms.Select(attrs={'class':'form-control','id':'city','placeholder':'Enter city'}))
    zip_code=forms.CharField( label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter zip code'}))
    address=forms.CharField( label='',widget=forms.Textarea(attrs={'class':'form-control', 'rows':'3','placeholder':'Enter full address'}))
    

    class Meta:
        model=ShippingInfo
        fields=('name','phone','email','state','city','zip_code','address')
        


class contact_form(forms.ModelForm):

    
    name=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email=forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    phone=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))
    subject=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}))
    massage=forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Massage'}))
    class Meta:
        model=Contacts
        fields=('__all__')
