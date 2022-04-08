from rest_framework import serializers
from .models import Restaurant, City, UserAccount

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields =('__all__')
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['city'] = instance.city.name
        rep['creator'] = instance.creator.name
        return rep

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields =('__all__')
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['creator'] = instance.creator.name
        return rep

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields =('email', 'name')