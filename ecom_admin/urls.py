
from django.contrib import admin
from django.urls import path
from ecom_admin import views

urlpatterns = [
    path('', views.dashboard,name=''),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('users/', views.users,name='users'),
    path('add-user/', views.add_user,name='add-user'),
    path('products/', views.products,name='products'),
    path('add-product/', views.add_product,name='add-product'),
    path('edit-product/<slug>', views.edit_product,name='edit-product'),
    path('delete-product/<int:pk>', views.delete_product,name='delete-product'),
    path('categories/', views.categories,name='categories'),
    path('add-category/', views.add_category,name='add-category'),
    path('edit-category/<int:pk>', views.edit_category,name='edit-category'),
    path('delete-category/<int:pk>', views.delete_category,name='delete-category'),

]
