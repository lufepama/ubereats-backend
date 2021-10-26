from django.contrib import admin
from django.urls import path
from .views import create_order, delete_order, update_order

urlpatterns = [
    path('create-order/', create_order, name='create_order'),
    path('delete-order/<str:orderId>/', delete_order, name='delete_order'),
    path('update-order/<str:orderId>/', update_order, name='update_order'),
]
