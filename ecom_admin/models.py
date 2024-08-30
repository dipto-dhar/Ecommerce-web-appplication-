
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
import datetime
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    first_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    image = models.ImageField(blank=True, default='profile.png',null=True)
    phone = models.IntegerField(null=True)
    groups=models.ForeignKey(Group,on_delete=models.CASCADE,default='4',null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.first_name + self.last_name
    
    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]
class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(default='blank-landscape.jpg',null=True)
    description=models.CharField(max_length=50)
    slug=AutoSlugField(populate_from=('name'),unique=True,null=True)
    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + self.last_name
    
class Product(models.Model):
    name=models.CharField(max_length=500,default='')
    sku=models.CharField(max_length=100,)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description=HTMLField(default='',blank=True)
    regular_price= models.DecimalField(max_digits=7,default=0,decimal_places=2)
    sale_price= models.DecimalField(max_digits=7,default=0, blank=True, null=True, decimal_places=2)
    on_sale=models.BooleanField(default=False)
    image=models.ImageField(upload_to='uploads/products', default='blank-sm.png', null=True)
    stock=models.BooleanField(default=True)
    date=models.DateField(default=datetime.datetime.now)
    slug = AutoSlugField(populate_from=('name'),unique=True,null=True, )
    def __str__(self) -> str:
        return self.name



# Pages Model


class Homepage(models.Model):
    # Main Slider
    slider=models.BooleanField(default=True)
    # Slide 1
    slide1_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    slide1_heading= models.CharField(max_length=500, blank=True, default='' )
    slide1_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    slide1_button_text= models.CharField(max_length=500, blank=True, default='' )
    slide1_button_link= models.CharField(max_length=1000, blank=True, default='')
    # Slide 1
    slide2_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    slide2_heading= models.CharField(max_length=500, blank=True, default='' )
    slide2_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    slide2_button_text= models.CharField(max_length=500, blank=True, default='' )
    slide2_button_link= models.CharField(max_length=1000, blank=True, default='')
    # Special Offer Section
    special_offer_banner=models.BooleanField(default=True)
    # Banner 1
    special_offer_banner1_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    special_offer_banner1_heading= models.CharField(max_length=500, blank=True, default='' )
    special_offer_banner1_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    special_offer_banner1_button_text= models.CharField(max_length=500, blank=True, default='' )
   
    special_offer_button_link1= models.CharField(max_length=1000, blank=True, default='' )
    # Banner 2
    special_offer_banner2_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    special_offer_banner2_heading= models.CharField(max_length=500, blank=True, default='' )
    special_offer_banner2_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    special_offer_banner2_button_text= models.CharField(max_length=500, blank=True, default='' )
    special_offer_button_link2= models.CharField(max_length=1000, blank=True, default='' )
    # Banner 3
    special_offer_banner3_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    special_offer_banner3_heading= models.CharField(max_length=500, blank=True, default='' )
    special_offer_banner3_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    special_offer_banner3_button_text= models.CharField(max_length=500, blank=True, default='' )
    special_offer_button_link3= models.CharField(max_length=1000, blank=True, default='' )
    # Trending Section
    tranding_section=models.BooleanField(default=True)
    tranding_banner=models.ImageField(blank=True, default='blank-landscape.jpg',)
    tranding_heading= models.CharField(max_length=500, blank=True, default='' )
    tranding_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    tranding_button_text= models.CharField(max_length=500, blank=True, default='' )
    tranding_button_link= models.CharField(max_length=1000, blank=True, default='' )
    
    # New Arrival Section
    new_arrival=models.BooleanField(default=True)
    # Banner 1
    new_arrival1_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    new_arrival1_heading= models.CharField(max_length=500, blank=True, default='' )
    new_arrival1_secondary_heading= models.CharField(max_length=500, blank=True, default='' )
    new_arrival1_button_text= models.CharField(max_length=500, blank=True, default='' )
    new_arrival1_button_link= models.CharField(max_length=1000, blank=True, default='')
    # Banner 1
    new_arrival2_image= models.ImageField(blank=True, default='blank-landscape.jpg',)
    new_arrival2_heading= models.CharField(max_length=500, blank=True, default='' )
    new_arrival2_secondary_heading= models.CharField(max_length=500, blank=True, default='', )
    new_arrival2_button_text= models.CharField(max_length=500, blank=True, default='', )
    new_arrival2_button_link= models.CharField(max_length=1000, blank=True, default='')

    # Trust & Support Section
    trust_box=models.BooleanField(default=True)
    # Box 1
    trust_box1_icon=models.ImageField(blank=True, default='blank-landscape.jpg',)
    trust_box1_heading= models.CharField(max_length=500, blank=True, default='' )
    trust_box1_secondary_text= models.CharField(max_length=600, blank=True, default='' )
    # Box 2
    trust_box2_icon=models.ImageField(blank=True, default='blank-landscape.jpg',)
    trust_box2_heading= models.CharField(max_length=500, blank=True, default='' )
    trust_box2_secondary_text= models.CharField(max_length=600, blank=True, default='' )
    # Box 3
    trust_box3_icon=models.ImageField(blank=True, default='blank-landscape.jpg',)
    trust_box3_heading= models.CharField(max_length=500, blank=True, default='' )
    trust_box3_secondary_text= models.CharField(max_length=600, blank=True, default='' )

 
class AboutPage(models.Model):
    page_title= models.CharField(max_length=500,blank=True, default='' )
    secendary_title= models.CharField(max_length=500,blank=True, default='' )
    page_banner=models.ImageField(blank=True, default='', null=True)
    page_content=HTMLField(default='',blank=True, )

class ContactPage(models.Model):
    page_title= models.CharField(max_length=500,blank=True, default='' )
    secendary_title= models.CharField(max_length=500,blank=True, default='' )
    page_banner=models.ImageField(blank=True, default='', null=True)
    page_content=HTMLField(default='',blank=True, )

class TermsPage(models.Model):
    page_title= models.CharField(max_length=500,blank=True, default='' )
    secendary_title= models.CharField(max_length=500,blank=True, default='' )
    page_banner=models.ImageField(blank=True, default='', null=True)
    page_content=HTMLField(default='',blank=True, )
    
class PrivacyPolicyPage(models.Model):
    page_title= models.CharField(max_length=500,blank=True, default='' )
    secendary_title= models.CharField(max_length=500,blank=True, default='' )
    page_banner=models.ImageField(blank=True, default='', null=True)
    page_content=HTMLField(default='',blank=True, )
