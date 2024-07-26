from django import forms
from .models import User
from django.contrib.auth.models import Group
from .models import *
from tinymce.widgets import TinyMCE


class create_user(forms.ModelForm):


    name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter full name'}))
    # username=forms.CharField( label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a username'}))
    email=forms.EmailField( label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a valid email'}))
    phone=forms.IntegerField(label='',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter a valid phone number'}))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    
    image=forms.ImageField( label='',required=False,widget=forms.FileInput(attrs={'class':'form-control file-upload-input','onchange':"readURL(this);"}))
    # groups=forms.ChoiceField(required=True, choices=option, widget=forms.Select(attrs={'class':'form-control'}))
    groups = forms.ModelChoiceField(queryset=Group.objects.all(),required=True, widget=forms.Select(attrs={'class':'form-control',}))
    description=forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control','rows':'6'}))
    date_joined=forms.TimeField(required=False)

    class Meta:
        model=User
        fields=('name','email','phone','password','groups','image','description')

class create_category(forms.ModelForm):

    name=forms.CharField( label='',widget=forms.TextInput(attrs={'class':'form-control','id':'categoryName'}))
    description=forms.CharField( label='',required=False,widget=forms.Textarea(attrs={'class':'form-control','id':'categoryDescription'}))
    image=forms.ImageField( label='',required=False,widget=forms.FileInput(attrs={'class':'form-control file-upload-input','onchange':"readURL(this);"}))

    class Meta:
        model=Category
        fields='__all__'

    
class create_product(forms.ModelForm):

    name=forms.CharField( label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Product title'}))
    sku=forms.CharField( label='', required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'SKU'}))
    regular_price=forms.DecimalField( label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Regular price'}))
    sale_price=forms.DecimalField( label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Sale price'}))
    # category=forms.ChoiceField( label='',widget=forms.Select(attrs={'class':'form-control'}))
    description=forms.CharField( label='',required=False,widget=TinyMCE(attrs={'class':'form-control','placeholder':'Product description'}))
    image=forms.ImageField( label='',required=False,widget=forms.FileInput(attrs={'class':'form-control file-upload-input','onchange':"readURL(this);"}))

    class Meta:
        model=Product
        fields=('name','regular_price','sale_price','on_sale','category','description','image','stock')
        widgets={

            'category': forms.Select(attrs={'class':'form-control','required':'False'}),
            'stock': forms.CheckboxInput(attrs={'id':'s1-14','class':'switch'}),
            'on_sale': forms.CheckboxInput(attrs={'id':'s1-14','class':'switch','onclick':'sale()'}),

        }
