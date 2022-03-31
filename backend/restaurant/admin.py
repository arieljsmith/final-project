from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')

admin.site.register(Restaurant, RestaurantAdmin)


