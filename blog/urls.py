
from django.contrib import admin
from django.urls import path
from .views import allblogs

urlpatterns = [
    path('', allblogs, name='allblogs'),
]
