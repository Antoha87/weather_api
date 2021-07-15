from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Weather
from .serializers import WeatherSerializer
from rest_framework.permissions import IsAuthenticated


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [IsAuthenticated]

# Create your views here.
