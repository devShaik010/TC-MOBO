from django.contrib import admin
from django.urls import path
from .views import *
from .ViewsFiles import index,signup,login

urlpatterns = [
    path('',index.home, name="home"),
    path('signup/',signup.sign_up, name="signup"),
    path('login/',login.login, name="login"),
    path('product/',product,name='product'),
    path('book/',book),
    path('cart/',cart, name="cart"),
    path('check-out/',check_out, name="check_out"),
    path('orders/',orders, name="orders"),
    path('payment/',payment_page, name="payment"),
    path('products/',searchBar, name="testing"),
    path('books/',searchBar2, name="testing2"),
    path('mobile/',phone_form, name="phone"),
    path('profile/',profile, name="technician"),
    path('update/',updates_profile, name="profile"),
    path('rqs/',rqs, name="submission"),
    path('rqs2/',rqs2, name="submission2"),
    path('rhis/',request_history, name="rhis"),
    path('settings',settings,name="settings")



]
