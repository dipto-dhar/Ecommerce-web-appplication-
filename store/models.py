from django.db import models
from ecom_admin.models import User
from django.db.models.signals import post_save



   
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

