from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from .serializers import DishSerializer
from .models import Dish
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_dishes(request, *args, **kwargs):
    dishes = Dish.objects.all()
    dishes_serializer = DishSerializer(dishes, many=True)
    return JsonResponse({'success': dishes_serializer.data}, status=status.HTTP_200_OK)
