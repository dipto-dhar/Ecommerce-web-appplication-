from django.contrib import admin
from .models import *
from .models import User

admin.site.register(Category)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)

    