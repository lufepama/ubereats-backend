from django.urls import path
from api.user import views

urlpatterns = [
    path('signup/', views.create_user, name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
]