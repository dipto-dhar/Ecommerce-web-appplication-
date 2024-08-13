from django.db import models
from ecom_admin.models import User
from django.db.models.signals import post_save


class ShippingInfo(models.Model):
   user=models.ForeignKey(User, on_delete=models.CASCADE)
   name=models.CharField(max_length=100,)
   phone=models.CharField(max_length=20)
   email=models.EmailField(max_length=100)
   state=models.CharField(max_length=100, null=True, blank=True)
   city=models.CharField(max_length=100, null=True, blank=True)
   zip_code=models.CharField(max_length=100, null=True)
   address=models.CharField(max_length=500)

   def __str__(self):
      return self.user.first_name +' '+ self.user.last_name
   
def add_shippinginfo(sender, instance, created, **kwargs):
   if created:
      user_shipinginfo=ShippingInfo(user=instance)
      user_shipinginfo.save()

post_save.connect(add_shippinginfo,sender=User)

class Cart(models.Model):
   user=models.OneToOneField(User, on_delete=models.CASCADE)
   user_cart=models.CharField(max_length=500)
   date_modified=models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.user.first_name + self.user.last_name
def create_cart(sender, instance, created, **kwargs):
   if created:
      user_cart=Cart(user=instance)
      user_cart.save()

post_save.connect(create_cart,sender=User)

