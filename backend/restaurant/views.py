from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RestaurantSerializer, CitySerializer, UserSerializer, TokenSerializer
from .models import Restaurant, City, UserAccount
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class RestaurantView(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

class CityView(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserAccount.objects.all()

class TokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer
