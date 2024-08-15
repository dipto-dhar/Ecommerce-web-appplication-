from django.db import models
from ecom_admin.models import User
from django.db.models.signals import post_save
from ecom_admin.models import Product

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


class OrderStatus(models.Model):
   status_name=models.CharField(max_length=30)
   status_description=models.CharField(max_length=30)
   update_date=models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.status_name

class Order(models.Model):
   user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
   order_id=models.CharField(max_length=50, null=True,blank=True, unique=True)
   name=models.CharField(max_length=50)
   email=models.EmailField(max_length=150)
   phone= models.CharField(max_length=20)
   shipping_address=models.TextField(max_length=1000)
   order_amount=models.DecimalField(max_digits=10,decimal_places=2)
   status= models.ForeignKey(OrderStatus, on_delete=models.CASCADE,null=True,default=1)
   date=models.DateTimeField(auto_now_add=True,null=True)

   def __str__(self):
      return self.name



class OrderItem(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
       return  self.product.name + " X " + str(self.quantity)