from django.contrib import admin
from .models import Restaurant, City, UserAccount

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')

class CityAdmin(admin.ModelAdmin):
    list_display = ('creator', 'name')

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'id', 'is_active')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(UserAccount, UserAdmin)


