from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import translation
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from .models import Order
from django.contrib.auth import get_user_model
import string
import random

User = get_user_model()

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_order(request, *args, **kwargs):
    try:
        data = request.data
        username = data['username']
        user = User.objects.get(username=username)
        order, created = Order.objects.get_or_create(customer=user)

        return JsonResponse({'success': 'Se ha generado el pedido', 'order': str(order.id)})
    except User.DoesNotExist:
        return JsonResponse({'Ha habido un error'})


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_order(request, orderId, *args, **kwargs):
    print('entree')
    query = Order.objects.filter(id=int(orderId))
    if query:
        order = query[0]
        order.delete()
        return JsonResponse({'success': 'Eliminado correctamente'})
    return JsonResponse({'error': 'No existe ningun pedido'})


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_order(request, orderId, *args, **kwargs):
    query = Order.objects.filter(id=int(orderId))
    if query:
        order = query[0]
        order.complete = True
        order.save()
        return JsonResponse({'success': 'Modificado correctamente'})
    return JsonResponse({'error': 'No existe ningun pedido'})
