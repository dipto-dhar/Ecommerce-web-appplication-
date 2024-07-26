from django.contrib import admin
from django.urls import path
from cart import views

urlpatterns = [
    path('', views.cart_summary,name=''),
    path('add/', views.add_to_cart,name='add-to-cart'),
    path('update-cart/', views.update_cart,name='update-cart'),
    path('remove/', views.add_to_cart,name='remove-from-cart'),
    
]