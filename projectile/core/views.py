from rest_framework import filters
from common.views import ListCreateAPICustomView, RetrieveUpdateDestroyAPICustomView
from core.permissions import IsSuperUser, IsAdminUser, CheckAnyPermission
from core.serializers import (
    OwnerUserWriteSerializer,
    OwnerUserReadSerializer,
    EmployeeUserReadSerializer,
    EmployeeUserWriteSerializer,
    EmployeeDesignationReadSerializer,
    EmployeeDesignationWriteSerializer,
    CustomerUserReadSerializer,
    CustomerUserWriteSerializer,
)
from core.choices import UserKind


class EmployeeDesignationListCreate(ListCreateAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser,)
    search_fields = ['name',]
    filter_backends = (filters.SearchFilter,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeeDesignationWriteSerializer
        return EmployeeDesignationReadSerializer

class EmployeeDesignationDetails(RetrieveUpdateDestroyAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeDesignationReadSerializer
        return EmployeeDesignationWriteSerializer


class OwnerUserListCreate(ListCreateAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser,)
    search_fields = ['first_name', 'last_name']
    filter_backends = (filters.SearchFilter,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OwnerUserWriteSerializer
        return OwnerUserReadSerializer

    def get_queryset(self):
        is_admin_user = IsAdminUser().has_permission(self.request, self.__class__)
        if is_admin_user:
            return super().get_queryset().filter(kind=UserKind.OWNER)
        return super().get_queryset().filter(kind=UserKind.OWNER)

    def perform_create(self, serializer, extra_fields=None):
        extra_fields = {
            'kind': UserKind.OWNER,
        }
        super().perform_create(serializer, extra_fields)


class OwnerUserDetails(RetrieveUpdateDestroyAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OwnerUserReadSerializer
        return OwnerUserWriteSerializer


class EmployeeUserListCreate(ListCreateAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser,)
    search_fields = ['first_name', 'last_name']
    filter_backends = (filters.SearchFilter,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeeUserWriteSerializer
        return EmployeeUserReadSerializer

    def get_queryset(self):
        is_admin_user = IsAdminUser().has_permission(self.request, self.__class__)
        if is_admin_user:
            return super().get_queryset().filter(kind=UserKind.EMPLOYEE)
        return super().get_queryset().filter(kind=UserKind.EMPLOYEE)

    def perform_create(self, serializer, extra_fields=None):
        extra_fields = {
            'kind': UserKind.EMPLOYEE,
            'owner_id': self.request.user.id,
        }
        super().perform_create(serializer, extra_fields)


class EmployeeUserDetails(RetrieveUpdateDestroyAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeUserReadSerializer
        return EmployeeUserWriteSerializer

class CustomerUserListCreate(ListCreateAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser,)
    search_fields = ['first_name', 'last_name']
    filter_backends = (filters.SearchFilter,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CustomerUserWriteSerializer
        return CustomerUserReadSerializer

    def get_queryset(self):
        is_admin_user = IsAdminUser().has_permission(self.request, self.__class__)
        if is_admin_user:
            return super().get_queryset().filter(kind=UserKind.CUSTOMER)
        return super().get_queryset().filter(kind=UserKind.CUSTOMER)

    def perform_create(self, serializer, extra_fields=None):
        extra_fields = {
            'kind': UserKind.CUSTOMER,
        }
        super().perform_create(serializer, extra_fields)


class CustomerUserDetails(RetrieveUpdateDestroyAPICustomView):
    permission_classes = (IsSuperUser | IsAdminUser,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerUserReadSerializer
        return CustomerUserWriteSerializer
