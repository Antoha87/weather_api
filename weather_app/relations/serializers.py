from rest_framework import serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from .models import Category, Goods, Tag, Cart


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name', 'uuid']


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = ['id', 'name', 'price']


class RecursiveField(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=True, read_only=True)
    num_of_tags = serializers.SerializerMethodField()
    num_of_goods = serializers.SerializerMethodField()
    children = RecursiveField(many=True)
    tags = TagSerializer(many=True, read_only=True)

    def get_num_of_tags(self, obj):
        return obj.tags.count()

    def get_num_of_goods(self, obj):
        return obj.goods.count()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'goods', 'num_of_goods', 'tags', 'num_of_tags', 'children']


class CartSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=True, read_only=False)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return obj.goods.all().aggregate(Sum('price'))

    class Meta:
        model = Cart
        fields = ['id', 'owner', 'goods', 'total_price']


class CreateCart(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id', 'owner', 'goods', 'delivery_type']
