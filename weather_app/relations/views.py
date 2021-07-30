from django.shortcuts import render
from .models import Category, Goods, Tag, Cart
from .serializers import CategorySerializer, GoodsSerializer, TagSerializer, CartSerializer, CreateCart
from .permission import IsOwner
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status, viewsets, filters
from django_filters import rest_framework as rest_filters


class GoodsFilter(rest_filters.FilterSet):
    min_price = rest_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = rest_filters.NumberFilter(field_name="price", lookup_expr='lte')
    name = rest_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price', 'name']


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = (rest_filters.DjangoFilterBackend,)
    filterset_class = GoodsFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.prefetch_related('goods', 'tags').select_related('parent')
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CartViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CartSerializer
    permission_classes = (IsOwner,)

    # Ensure a user sees only own Cart objects.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Cart.objects.filter(owner=user)
        raise PermissionDenied()

    # Set user as owner of a Carts object.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CreateCartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    permission_classes = (IsOwner,)
    serializer_class = CreateCart
