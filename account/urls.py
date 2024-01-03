from django.urls import path
from .views import *

app_name="account"

urlpatterns=[
    path("" , home , name="home"),
    path("login/" , login_view , name="login"),
    path("logout_view/" , logout_view , name="logout_view"),
    path("my-notification/" , my_notifications , name="my-notification"),
]