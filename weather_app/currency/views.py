from django.shortcuts import render
from rest_framework import viewsets
from .models import CurrencyData, Currency, CurrencyAverage
from .serializers import CurrencyDataSerializer, CurrencySerializer, CurrencyAverageSerializer
from rest_framework import generics, status, viewsets, filters
from django_filters import rest_framework as rest_filters
from .models import STATUS_CHOICES


class CryptoDataFilter(rest_filters.FilterSet):
    name = rest_filters.CharFilter(field_name='name', lookup_expr='icontains')
    created = rest_filters.DateFilter(field_name='created', lookup_expr='gte')
    status = rest_filters.ChoiceFilter(field_name='status', choices=STATUS_CHOICES)

    class Meta:
        model = CurrencyData
        fields = ['name', 'created', 'status']


class CryptoDataViewSet(viewsets.ModelViewSet):
    queryset = CurrencyData.objects.all()
    serializer_class = CurrencyDataSerializer
    filter_backends = (rest_filters.DjangoFilterBackend,)
    filterset_class = CryptoDataFilter


class CryptoViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrencyAverageViewSet(viewsets.ModelViewSet):
    queryset = CurrencyAverage.objects.all()
    serializer_class = CurrencyAverageSerializer
