from django.contrib import admin
from .models import Restaurant

class ResturantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')

admin.site.register(Restaurant, ResturantAdmin)


