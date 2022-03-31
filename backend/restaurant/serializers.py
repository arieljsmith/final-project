from rest_framework import serializers
from .models import Restaurant, City, UserAccount

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields =('id', 'name', 'city')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields =('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields =('email', 'name')