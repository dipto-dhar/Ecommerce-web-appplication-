
from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('', views.home,name=''),
    path('home/', views.home,name='home'),
    path('login/', views.user_login,name='login'),
    path('logout/', views.user_logout,name='logout'), 
    path('my-account/', views.my_account,name='my-account'),
    path('my-account/update/', views.user_update,name='update_account'),
    path('my-account/update/password/', views.password_update,name='update_password'),
    path('register/', views.user_register,name='register'),
    path('shop/', views.shop,name='shop'),
    path('shop/<slug>', views.shop_by,name='shop'),
    path('category/', views.category,name='category'),
    path('product/<slug>', views.product,name='product'),
    path('wishlist/', views.wishlist,name='wishlist'),
    path('checkout/', views.checkout,name='checkout'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
   
    
    # path('/', views.,name=''),

    # path('dashboard/', views.dashboard,name='dashboard'),
    # path('users/', views.users,name='users'),
    # path('add-user/', views.add_user,name='add-user'),
    # path('products/', views.products,name='products'),
    # path('add-product/', views.add_product,name='add-product'),
    # path('edit-product/<slug>', views.edit_product,name='edit-product'),
    # path('delete-product/<int:pk>', views.delete_product,name='delete-product'),
    # path('categories/', views.categories,name='categories'),
    # path('add-category/', views.add_category,name='add-category'),
    # path('edit-category/<int:pk>', views.edit_category,name='edit-category'),
    # path('delete-category/<int:pk>', views.delete_category,name='delete-category'),

]
