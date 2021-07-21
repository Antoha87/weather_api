from django.shortcuts import render
from .models import Category, Goods, Tag
from .serializers import CategorySerializer, GoodsSerializer, TagSerializer
from rest_framework import generics, status, viewsets, filters


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().prefetch_related('goods', 'tags')
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
