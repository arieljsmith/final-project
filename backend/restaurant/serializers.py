from rest_framework import serializers
from .models import Restaurant, City, UserAccount
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

class RestaurantSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.name')
    class Meta:
        model = Restaurant
        fields =('creator', 'city', 'name', 'id', 'creator_id', 'image', 'cuisine', 'price')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['city'] = instance.city.name
        rep['city_id'] = instance.city.id
        rep['city_creator_id'] = instance.city.creator.id
        rep['creator'] = instance.creator.name
        rep['creator_id'] = instance.creator.id
        return rep

    def validate_city(self, value):
        # checks if user is creator of city 
        value_id = value.id
        city_obj = City.objects.get(id=value_id)
        user = self.context['request'].user

        if not city_obj.creator == user:
            raise serializers.ValidationError('You do not have permission to do that')
        return value

class RestaurantDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields =('id', 'image', 'cuisine', 'price')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['creator'] = instance.creator.name
        rep['creator_id'] = instance.creator.id
        return rep


class CitySerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.name')
    class Meta:
        model = City
        fields =('id', 'creator', 'name')
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['creator'] = instance.creator.name
        rep['creator_id'] = instance.creator.id
        return rep

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('email', 'name','id', 'password', 'image', 'location')

    def validate_password(self, value: str) -> str:
        # this changes user password from plaintext to a hashed value
        return make_password(value)

class TokenSerializer(TokenObtainPairSerializer):

    def get_token(cls, user):
        token = super(TokenSerializer, cls).get_token(user)

        #add custom claims
        token['email'] = user.email
        return token