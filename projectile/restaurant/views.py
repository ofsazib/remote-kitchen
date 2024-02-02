from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from common.views import ListCreateAPICustomView, RetrieveUpdateDestroyAPICustomView
from core.permissions import IsSuperUser, IsAdminUser, IsOwner
from restaurant.serializers import (
    RestaurantReadSerializer,
    RestaurantWriteSerializer,
    MenuReadSerializer,
    MenuWriteSerializer,
    MenuItemReadSerializer,
    MenuItemWriteSerializer,
    OrderPayloadSerializer,
    OrderReadSerializer,
)
from core.choices import UserKind
from .filters import MenuListFilter


class RestaurantListCreate(ListCreateAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser | IsOwner,)
    search_fields = ['name',]
    filter_backends = (filters.SearchFilter,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RestaurantWriteSerializer
        return RestaurantReadSerializer

    def perform_create(self, serializer, extra_fields=None):
        extra_fields = {
            'owner_id': self.request.user.id,
        }
        super().perform_create(serializer, extra_fields)

    def get_queryset(self):
        is_admin_user = IsAdminUser().has_permission(self.request, self.__class__)
        if is_admin_user or self.request.user.is_superuser:
            return super().get_queryset()
        return super().get_queryset().filter(owner_id=self.request.user.id)

class RestaurantDetails(RetrieveUpdateDestroyAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser | IsOwner,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RestaurantReadSerializer
        return RestaurantWriteSerializer


class MenuListCreate(ListCreateAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser | IsOwner,)
    search_fields = ['name',]
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_class = MenuListFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MenuWriteSerializer
        return MenuReadSerializer

    def perform_create(self, serializer, extra_fields=None):
        extra_fields = {
            'owner_id': self.request.user.id,
        }
        super().perform_create(serializer, extra_fields)

    def get_queryset(self):
        is_admin_user = IsAdminUser().has_permission(self.request, self.__class__)
        if is_admin_user or self.request.user.is_superuser:
            return super().get_queryset()
        return super().get_queryset().filter(owner_id=self.request.user.id)

class MenuDetails(RetrieveUpdateDestroyAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser | IsOwner,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MenuReadSerializer
        return MenuWriteSerializer


class MenuItemListCreate(ListCreateAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser | IsOwner,)
    search_fields = ['name',]
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MenuItemWriteSerializer
        return MenuItemReadSerializer

    def perform_create(self, serializer, extra_fields=None):
        extra_fields = {
            'owner_id': self.request.user.id,
        }
        super().perform_create(serializer, extra_fields)

    def get_queryset(self):
        is_admin_user = IsAdminUser().has_permission(self.request, self.__class__)
        if is_admin_user or self.request.user.is_superuser:
            return super().get_queryset()
        return super().get_queryset().filter(owner_id=self.request.user.id)

class MenuItemDetails(RetrieveUpdateDestroyAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser | IsOwner,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MenuItemReadSerializer
        return MenuItemWriteSerializer

class OrderListCreate(ListCreateAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser | IsOwner,)
    search_fields = ['name',]
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderPayloadSerializer
        return OrderReadSerializer

    def perform_create(self, serializer, extra_fields=None):
        extra_fields = {
            'user_id': self.request.user.id,
        }
        super().perform_create(serializer, extra_fields)

    def post(self, request):
        try:
            serializer = OrderPayloadSerializer(
                data=request.data, context={'request': request}
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    created_by_id=self.request.user.id,
                )
                return Response(
                    {"message": "Order Create success"},
                    status=status.HTTP_201_CREATED
                )

        except Exception as exception:
            content = {'error': '{}'.format(exception)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # def get_queryset(self):
    #     is_admin_user = IsAdminUser().has_permission(self.request, self.__class__)
    #     if is_admin_user or self.request.user.is_superuser:
    #         return super().get_queryset()
    #     return super().get_queryset().filter(owner_id=self.request.user.id)
