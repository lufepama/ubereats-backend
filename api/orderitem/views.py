from copy import error
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from .serializers import OrderItemSerializer, AddOrderItemSerializer
from .models import OrderItem
from api.order.models import Order
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_orderitem_list(request, orderId, *args, **kwargs):
    try:
        query = Order.objects.get(id=int(orderId))
        order_item = OrderItem.objects.filter(order=query)
        order_item_serializer = OrderItemSerializer(order_item, many=True)
        return JsonResponse({'success': order_item_serializer.data, 'length': len(order_item)}, status=status.HTTP_200_OK)
    except error:
        return JsonResponse({'error': error})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_orderitem_list(request, *args, **kwargs):

    data = request.data
    context = {
        "dish": data['dishId'],
        "order": data['orderId'],
    }

    order_item_serializer = AddOrderItemSerializer(
        data=context, context=context)
    if order_item_serializer.is_valid():
        order_item_serializer.save()
        return JsonResponse({'success': 'Se ha añadido correctamente'})
    else:
        return JsonResponse({'error': 'Ha habido un problema...'})
