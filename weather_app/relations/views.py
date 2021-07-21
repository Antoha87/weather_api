from django.shortcuts import render
from .models import Category, Goods, Tag
from .serializers import CategorySerializer, GoodsSerializer, TagSerializer
from rest_framework import generics, status, viewsets


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().prefetch_related('goods')
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().prefetch_related('categories', 'categories__goods')
    serializer_class = TagSerializer
