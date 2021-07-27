from rest_framework import viewsets
from rest_framework import permissions
from .models import Cart
from .serializers import CartSerializer


class IsOwner(permissions.BasePermission):
    message = 'Not an owner.'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
