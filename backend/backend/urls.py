from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurants import views

router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantView, 'restaurant')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
