from django.shortcuts import render
from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly
from .serializers import RestaurantSerializer, CitySerializer, UserSerializer, TokenSerializer
from .models import Restaurant, City, UserAccount
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView


class RestaurantView(viewsets.ModelViewSet):
    permissions_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class CityView(viewsets.ModelViewSet):
    permissions_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    
class UserView(viewsets.ModelViewSet):
    permissions_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserSerializer
    queryset = UserAccount.objects.all()

class TokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer
