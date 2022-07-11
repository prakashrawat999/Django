from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.loginUser, name="loginUser"),
    path('logout', views.logoutUser, name="logoutUser")
]