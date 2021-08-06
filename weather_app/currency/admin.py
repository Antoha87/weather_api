from django.contrib import admin
from .models import CurrencyData, Currency, CurrencyAverage, User


class CurrencyDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'status')
    search_fields = ('name', 'status')
    list_filter = ('name',)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'price')
    search_fields = ('name', 'symbol')
    list_filter = ('name',)


class CurrencyAverageAdmin(admin.ModelAdmin):
    list_display = ('name', 'avg_value',)
    search_fields = ('name',)
    list_filter = ('name',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(CurrencyData, CurrencyDataAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(CurrencyAverage, CurrencyAverageAdmin)
admin.site.register(User, UserAdmin)
