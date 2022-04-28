from django.shortcuts import render
from rest_framework import viewsets

import restaurant

from .permissions import IsOwnerOrReadOnly
from .serializers import RestaurantSerializer, CitySerializer, UserSerializer, TokenSerializer, RestaurantDetailSerializer
from .models import Restaurant, City, UserAccount
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from restaurant import serializers



class RestaurantView(viewsets.ModelViewSet):
    permissions_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class RestaurantDetailView(APIView):
    permissions_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    serializer_class = RestaurantDetailSerializer
    
    context_object_name = 'restaurant'

    def get_object(self, restaurant_id, creator_id):
        try:
            return Restaurant.objects.get(id=restaurant_id, creator=creator_id)
        except Restaurant.DoesNotExist:
            return None

    def get(self, request, restaurant_id, *args, **kwargs):
        restaurant_instance = self.get_object(restaurant_id, request.user.id)
        if not restaurant_instance:
            return Response(
                {'res': 'Object with restaurant id does not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = RestaurantDetailSerializer(restaurant_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, restaurant_id, *args, **kwargs):
        restaurant_instance = self.get_object(restaurant_id, request.user.id)
        if not restaurant_instance:
            return Response(
                {'res': 'Object with restaurant id does not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'image': request.data.get('image'),
            'cuisine': request.data.get('cuisine'),
            'price': request.data.get('price')
        }
        serializer = RestaurantDetailSerializer(instance=restaurant_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, restaurant_id, *args, **kwargs):
        restaurant_instance = self.get_object(restaurant_id, request.user.id)
        if not restaurant_instance:
            return Response(
                {'res': 'Object with restaurant id does not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )
        restaurant_instance.delete()
        return Response(
            {'res': 'Restaurant Deleted'},
            status=status.HTTP_200_OK
        )


class CityView(viewsets.ModelViewSet):
    permissions_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    
class UserView(viewsets.ModelViewSet):
    permissions_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = UserAccount.objects.all()

class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
