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
    sale_price=forms.DecimalField( label='', required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Sale price'}))
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


from django import forms
from .models import Homepage

class HomepageForm(forms.ModelForm):
    class Meta:
        model = Homepage
        fields = [
            'slider', 'slide1_image', 'slide1_heading', 'slide1_secondary_heading', 'slide1_button_text', 'slide1_button_link',
            'slide2_image', 'slide2_heading', 'slide2_secondary_heading', 'slide2_button_text', 'slide2_button_link',
            'special_offer_banner', 'special_offer_banner1_image', 'special_offer_banner1_heading', 'special_offer_banner1_secondary_heading', 'special_offer_banner1_button_text', 'special_offer_button_link1',
            'special_offer_banner2_image', 'special_offer_banner2_heading', 'special_offer_banner2_secondary_heading', 'special_offer_banner2_button_text', 'special_offer_button_link2',
            'special_offer_banner3_image', 'special_offer_banner3_heading', 'special_offer_banner3_secondary_heading', 'special_offer_banner3_button_text', 'special_offer_button_link3',
            'tranding_section', 'tranding_banner', 'tranding_heading', 'tranding_secondary_heading', 'tranding_button_text', 'tranding_button_link',
            'special_offer_banner','new_arrival','new_arrival1_image', 'new_arrival1_heading', 'new_arrival1_secondary_heading', 'new_arrival1_button_text', 'new_arrival1_button_link',
            'new_arrival2_image', 'new_arrival2_heading', 'new_arrival2_secondary_heading', 'new_arrival2_button_text', 'new_arrival2_button_link',
            'trust_box', 'trust_box1_icon', 'trust_box1_heading', 'trust_box1_secondary_text',
            'trust_box2_icon', 'trust_box2_heading', 'trust_box2_secondary_text',
            'trust_box3_icon', 'trust_box3_heading', 'trust_box3_secondary_text'
        ]
        
        widgets = {
        'slider': forms.CheckboxInput(attrs={'id':'s1-14','class':'switch slider-switch','onclick':"toggleCardBody('slider-body', 'slider-header', 'slider-switch')"}),
        'slide1_image': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),  # Already FileInput
        'slide1_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heading'}),
        'slide1_secondary_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary heading'}),
        'slide1_button_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter button text'}),
        'slide1_button_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://......'}),

        'slide2_image': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),  # Changed from ClearableFileInput to FileInput
        'slide2_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heading'}),
        'slide2_secondary_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary heading'}),
        'slide2_button_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter button text'}),
        'slide2_button_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://......'}),

        'special_offer_banner': forms.CheckboxInput(attrs={'id':'s1-14','class':'switch special-switch','onclick':"toggleCardBody('banner-body', 'banner-header', 'special-switch')"}),
        'special_offer_banner1_image': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),  # Changed
        'special_offer_banner1_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heading'}),
        'special_offer_banner1_secondary_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary heading'}),
        'special_offer_banner1_button_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter button text'}),
        'special_offer_button_link1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://......'}),

        'special_offer_banner2_image': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),  # Changed
        'special_offer_banner2_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heading'}),
        'special_offer_banner2_secondary_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary heading'}),
        'special_offer_banner2_button_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter button text'}),
        'special_offer_button_link2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://......'}),

        'special_offer_banner3_image': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),  # Changed
        'special_offer_banner3_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heading'}),
        'special_offer_banner3_secondary_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary heading'}),
        'special_offer_banner3_button_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter button text'}),
        'special_offer_button_link3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://......'}),

        'tranding_section': forms.CheckboxInput(attrs={'id':'s1-14','class':'switch tranding-switch','onclick':"toggleCardBody('tranding-body', 'tranding-header', 'tranding-switch')"}),
        'tranding_banner': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),  # Changed
        'tranding_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heading'}),
        'tranding_secondary_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary heading'}),
        'tranding_button_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter button text'}),
        'tranding_button_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://......'}),

        'new_arrival': forms.CheckboxInput(attrs={'id':'s1-14','class':'switch arrival-switch','onclick':"toggleCardBody('new_arrival-body', 'new_arrival-header', 'arrival-switch')"}),
        'new_arrival1_image': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),  # Changed
        'new_arrival1_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heading'}),
        'new_arrival1_secondary_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary heading'}),
        'new_arrival1_button_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter button text'}),
        'new_arrival1_button_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://......'}),

        'new_arrival2_image': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),  # Changed
        'new_arrival2_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heading'}),
        'new_arrival2_secondary_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary heading'}),
        'new_arrival2_button_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter button text'}),
        'new_arrival2_button_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://......'}),

        'trust_box': forms.CheckboxInput(attrs={'id':'s1-14','class':'switch trust-switch','onclick':"toggleCardBody('trust-body', 'trust-header', 'trust-switch')"}),
        'trust_box1_icon': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),  # Changed
        'trust_box1_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heading'}),
        'trust_box1_secondary_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary text'}),

        'trust_box2_icon': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),  # Changed
        'trust_box2_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heading'}),
        'trust_box2_secondary_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary text'}),

        'trust_box3_icon': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),  # Changed
        'trust_box3_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heading'}),
        'trust_box3_secondary_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary text'}),
}




class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = ['page_title', 'secendary_title', 'page_banner', 'page_content']
        widgets = {
            'page_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter page title'}),
            'secendary_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary title'}),
            'page_banner':forms.FileInput(attrs={'class':'file-upload-input','onchange':'readURL(this);'}),
            'page_content': TinyMCE(attrs={'class': 'form-control', 'placeholder': 'Enter page content'}),
        }

class ContactPageForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = ['page_title', 'secendary_title', 'page_banner', 'page_content']
        widgets = {
            'page_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter page title'}),
            'secendary_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary title'}),
            'page_banner': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),
            'page_content': TinyMCE(attrs={'class': 'form-control', 'placeholder': 'Enter contact information'}),
        }



class TermsPageForm(forms.ModelForm):
    class Meta:
        model = TermsPage
        fields = ['page_title', 'secendary_title', 'page_banner', 'page_content']
        widgets = {
            'page_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter page title'}),
            'secendary_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary title'}),
            'page_banner': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),
            'page_content': TinyMCE(attrs={'class': 'form-control', 'placeholder': 'Enter Details'}),
        }
class PrivacyPolicyPageForm(forms.ModelForm):
    class Meta:
        model = PrivacyPolicyPage
        fields = ['page_title', 'secendary_title', 'page_banner', 'page_content']
        widgets = {
            'page_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter page title'}),
            'secendary_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary title'}),
            'page_banner': forms.FileInput(attrs={'class':'file-upload-input','onchange':"readURL(this);"}),
            'page_content': TinyMCE(attrs={'class': 'form-control', 'placeholder': 'Enter Details'}),
        }