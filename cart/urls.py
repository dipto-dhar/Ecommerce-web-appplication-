from django.contrib import admin
from django.urls import path
from cart import views

urlpatterns = [
    path('', views.cart_summary,name='cart'),
    path('add/', views.add_to_cart,name='add_cart'),
     path('update-cart/', views.update_cart, name='update-cart'),
    path('remove/', views.delete_cart,name='remove-from-cart'),
    
]