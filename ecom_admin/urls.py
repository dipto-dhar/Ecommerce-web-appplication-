
from django.contrib import admin
from django.urls import path
from ecom_admin import views
from django.conf.urls import include
urlpatterns = [
    path('', views.dashboard,name=''),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('users/', views.users,name='users'),
    path('add-user/', views.add_user,name='add-user'),
    path('edit-user/<int:pk>', views.edit_user,name='edit-user'),
    path('delete-user/<int:pk>', views.delete_user,name='delete-user'),
    path('contacts/', views.contacts,name='contacts'),
    path('delete-contact/<int:pk>', views.delete_contact,name='delete-contact'),
    path('orders/', views.orders,name='orders'),
    path('order/<order_id>', views.single_order,name='order'),
    path('delete-order/<order_id>', views.delete_order,name='delete-order'),
    path('products/', views.products,name='products'),
    path('add-product/', views.add_product,name='add-product'),
    path('edit-product/<slug>', views.edit_product,name='edit-product'),
    path('delete-product/<int:pk>', views.delete_product,name='delete-product'),
    path('delete-products/', views.bulk_delete,name='delete-products'),
    path('categories/', views.categories,name='categories'),
    path('add-category/', views.add_category,name='add-category'),
    path('edit-category/<int:pk>', views.edit_category,name='edit-category'),
    path('delete-category/<int:pk>', views.delete_category,name='delete-category'),
    path('shipping-zones/', views.shipping_zones, name='shipping-zones'),
    path('delete-shipping-zone/<int:zone_id>/', views.delete_shipping_zone, name='delete-shipping-zone'),
    # path('edit-shipping-zone/<int:id>/', views.edit_shipping_zone, name='edit-shipping-zone'),
    path('add_shipping_zone/', views.add_shipping_zone,name='add_shipping_zone'),
    path('add-shipping-zone/', views.shipping_zone_submit,name='add-shipping-zone'),
    path('pages/home', views.update_homepage,name='update-home'),
    path('pages/about', views.update_aboutpage,name='update-about'),
    path('pages/contact', views.update_contactpage,name='update-contact'),
    path('pages/terms-&-condition', views.update_termspage,name='update-terms'),
    path('pages/privacy-policy', views.update_privacypage,name='update-privacy'),
    path('settings/', views.settings,name='settings'),

]
