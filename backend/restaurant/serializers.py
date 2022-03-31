from rest_framework import serializers
from .models import Restaurant, City, UserAccount

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields =('id', 'name', 'city')
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['city'] = instance.city.name
        return rep

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields =('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields =('email', 'name')