from django.contrib import admin
from django.urls import path
from . import views
# http://127.0.0.1:8000/user/register
urlpatterns = [
    path('', views.user_register,name='register'),
  
]