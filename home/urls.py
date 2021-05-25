
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login_page', views.login_page, name="login_page"),
    path('registration_page', views.registration_page, name="registration_page"),
    path('product_list', views.product_list, name='product_list'),
    path('shop_list',views.shop_list, name="shop_list")
]
