from django.shortcuts import render
from rest_framework import viewsets
from .models import CurrencyData, Currency
from .serializers import CurrencyDataSerializer, CurrencySerializer


class CryptoDataViewSet(viewsets.ModelViewSet):
    queryset = CurrencyData.objects.all()
    serializer_class = CurrencyDataSerializer


class CryptoViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
