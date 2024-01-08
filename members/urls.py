from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('login_user',views.loginUser,name="login"),
    path('',views.index,name="index"),
    path('logout_user',views.logout1,name="login"),
]
