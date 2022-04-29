from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)
from restaurant import views
from restaurant.views import BlacklistTokenUpdateView, RestaurantDetailView, UserDetailView

router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantView, 'restaurant')
router.register(r'cities', views.CityView, 'city')
router.register(r'users', views.UserView, 'user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
    path('api/auth/', include('rest_framework.urls')),
    path('api/update/<int:restaurant_id>/', RestaurantDetailView.as_view(), name='update'),
    path('api/users/update/<int:user_id>/', UserDetailView.as_view(), name='update_user'),
]
