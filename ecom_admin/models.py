
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
    name = models.CharField(max_length=255, blank=True, default='')
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
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]
class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(default='blank-sm.png',null=True)
    description=models.CharField(max_length=50)
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
    name=models.CharField(max_length=500)
    sku=models.CharField(max_length=100,)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description=HTMLField(default='',blank=True)
    regular_price= models.DecimalField(max_digits=7,default=0,decimal_places=2)
    sale_price= models.DecimalField(max_digits=7,default=0,decimal_places=2)
    on_sale=models.BooleanField(default=False)
    image=models.ImageField(upload_to='uploads/products', default='blank-sm.png', null=True)
    stock=models.BooleanField(default=True)
    date=models.DateField(default=datetime.datetime.now)
    slug = AutoSlugField(populate_from=('name'),unique=True,null=True)
    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    address=models.CharField(max_length=200,default='')
    phone= models.CharField(max_length=15)
    date=models.DateField(default=datetime.datetime.now)
    status=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.customer