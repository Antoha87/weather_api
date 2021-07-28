from django.contrib import admin
from .models import CurrencyData, Currency


class CurrencyDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'status')
    search_fields = ('name', 'status')
    list_filter = ('name',)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'price')
    search_fields = ('name', 'symbol')
    list_filter = ('name',)


admin.site.register(CurrencyData, CurrencyDataAdmin)
admin.site.register(Currency, CurrencyAdmin)
