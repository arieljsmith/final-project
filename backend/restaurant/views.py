from django.shortcuts import render
from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly
from .serializers import RestaurantSerializer, CitySerializer, UserSerializer, TokenSerializer
from .models import Restaurant, City, UserAccount
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



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
