from rest_framework import serializers
from .models import Category, Goods, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name', 'uuid']


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'name', 'price']


class CategorySerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=True, read_only=True)
    num_of_tags = serializers.SerializerMethodField()
    num_of_goods = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)

    def get_num_of_tags(self, obj):
        return obj.tags.count()

    def get_num_of_goods(self, obj):
        return obj.goods.count()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'goods', 'num_of_goods', 'tags', 'num_of_tags']
