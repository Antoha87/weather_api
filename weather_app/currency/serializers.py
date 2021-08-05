from rest_framework import serializers
from .models import CurrencyData, Currency, CurrencyAverage


class CurrencyDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurrencyData
        fields = ['id', 'name', 'created', 'status', 'data']


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ['name', 'symbol', 'price', 'change_30d', 'change_60d', 'change_90d', 'max_supply', 'circulating_supply']


class CurrencyCoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ['name', 'symbol', 'price', 'change_30d', 'change_60d', 'change_90d', 'max_supply', 'circulating_supply']


class CurrencyAverageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurrencyAverage
        fields = ['id', 'name', 'avg_value']
