from django.shortcuts import render
from .models import Category, Goods
from .serializers import CategorySerializer, GoodsSerializer
from rest_framework import generics, status, viewsets

# Create your views here.


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().prefetch_related('categories')
    serializer_class = CategorySerializer
