from django.contrib import admin
from .models import Weather


class WeatherAdmin(admin.ModelAdmin):
    list_filter = ('location', 'loc_time', 'temperature')
    search_fields = ('location', 'temperature')
    list_display = ('location', 'loc_time', 'temperature')

admin.site.register(Weather, WeatherAdmin)

# Register your models here.
