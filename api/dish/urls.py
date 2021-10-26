from django.contrib import admin
from django.urls import path
from .views import get_dishes

urlpatterns = [
    path('get-dishes/', get_dishes, name='get_dishes')
]
