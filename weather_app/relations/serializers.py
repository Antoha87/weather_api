from rest_framework import serializers
from .models import Category, Goods


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'name', 'price']


class CategorySerializer(serializers.ModelSerializer):
    categories = GoodsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'categories']
