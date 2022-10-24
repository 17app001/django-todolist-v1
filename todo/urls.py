from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo,name='todo'),  
    path('create/',views.createtodo,name='createtodo'),
    path('view/<int:id>',views.viewtodo,name='viewtodo'),
    path('completed/',views.completed,name='completed')
]