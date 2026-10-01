from django.urls import path 
from .views import *
urlpatterns=[
    path('',home, name="home"),
    path('login/',login, name="login"),
    path('register/',register, name="register"),
    path('dashboard/',dashboard, name="dashboard"),
    path('predict/',predict, name="predict"),
    path('registerForm/',registerForm, name="registerForm"),
    path('loginForm/',loginForm, name="loginForm"),
    path('logout/',logout, name="logout"),
]


