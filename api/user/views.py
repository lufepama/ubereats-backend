from api.order.models import Order
from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from .models import User
# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request, *args, **kwargs):
    user_data = request.data
    new_user_serializer = UserSerializer(data=user_data, context=user_data)

    if new_user_serializer.is_valid():
        new_user_serializer.save()
        return Response({'success': 'Cuenta creada satisfactoriamente'}, status=status.HTTP_201_CREATED)
    else:
        return Response(new_user_serializer.errors)


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        login_serializer = self.serializer_class(
            data=request.data, context={'request': request})

        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                order, created = Order.objects.get_or_create(
                    customer=user, complete=False)
                if created:
                    return Response({
                        'success': {
                            'token': token.key,
                            'username': user.username,
                            'firstName': user.first_name,
                            'lastName': user.last_name,
                            'email': user.email,
                            'orderId': order.id,
                            'success': 'Inicio de sesión exitoso'
                        }

                    }, status=status.HTTP_201_CREATED)
                else:
                    token.delete()
                    new_token = Token.objects.create(user=user)
                    return Response({
                        'token': new_token.key,
                        'username': user.username,
                        'firstName': user.first_name,
                        'lastName': user.last_name,
                        'email': user.email,
                        'orderId': order.id,
                        'success': 'Inicio de sesión exitoso'
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'El usuario no puede inciar sesion'}, status=status.HTTP_303_SEE_OTHER)
        else:
            return Response(login_serializer.errors, status=status.HTTP_303_SEE_OTHER)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    user_data = request.data
    try:
        user = User.objects.get(username=user_data['username'])
        token_user = Token.objects.get(user=user)
        if token_user.key == user_data['token']:
            token_user.delete()
            return Response({'success': 'Has cerrado sesión correctamente'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No puedes cerrar sesión, te faltan las credenciales'}, status=status.HTTP_303_SEE_OTHER)
    except User.DoesNotExist:
        return Response({'error': 'Ha habido un error'}, status=status.HTTP_303_SEE_OTHER)
