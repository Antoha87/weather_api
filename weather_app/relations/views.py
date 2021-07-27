from django.shortcuts import render
from .models import Category, Goods, Tag, Cart
from .serializers import CategorySerializer, GoodsSerializer, TagSerializer, CartSerializer, CreateCart
from rest_framework import generics, status, viewsets, filters
from .permission import IsOwner
from rest_framework.exceptions import PermissionDenied


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


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
