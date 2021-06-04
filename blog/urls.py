
from django.contrib import admin
from django.urls import path
from .views import allblogs, detail

urlpatterns = [
    path('', allblogs, name='allblogs'),
    path('<int:blog_id>', detail, name='detail'),
]