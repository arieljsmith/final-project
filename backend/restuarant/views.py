from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RestaurantSerializer, CitySerializer
from .models import Restaurant, City

class RestaurantView(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

class CityView(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()