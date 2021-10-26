from django.contrib import admin
from django.urls import path
from .views import add_orderitem_list, get_orderitem_list

urlpatterns = [
    path('add-orderitem-list/', add_orderitem_list, name='add_orderitem_list'),
    path('get-orderitem-list/<str:orderId>/', get_orderitem_list, name='get_orderitem_list'),
]
