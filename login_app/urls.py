from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("login",views.signin, name="login"),
    path("register",views.signup, name="register"),
    path("signin",views.signin, name="signin"),
    path("signup",views.signup, name="signup"),
]