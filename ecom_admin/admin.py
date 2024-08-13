from django.contrib import admin
from .models import *
from .models import User
from store.models import *

admin.site.register(Category)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(ShippingInfo)


class CartInline(admin.StackedInline):
    model=Cart

class ShippingInfoInline(admin.StackedInline):
    model=ShippingInfo



class UserAdmin(admin.ModelAdmin):
    model=User
    field=('first_name','last_name','email','phone')
    inlines=[CartInline,ShippingInfoInline]

admin.site.unregister(User)
admin.site.register(User,UserAdmin)