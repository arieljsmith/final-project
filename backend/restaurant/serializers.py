from rest_framework import serializers
from .models import Restaurant, City, UserAccount
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields =('__all__')
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['city'] = instance.city.name
        rep['creator'] = instance.creator.name
        rep['creator_id'] = instance.creator.id
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
        fields =('email', 'name', 'id')

class TokenSerializer(TokenObtainPairSerializer):

    def get_token(cls, user):
        token = super(TokenSerializer, cls).get_token(user)

        #add custom claims
        token['email'] = user.email
        return token