from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('dish/',include('api.dish.urls')),
    path('orderitem/',include('api.orderitem.urls')),
    path('order/',include('api.order.urls')),
    path('user/',include('api.user.urls')),
]
