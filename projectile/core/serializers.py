from rest_framework import serializers
from core.models import (
    User,
    EmployeeDesignation,
)

class EmployeeDesignationWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeDesignation
        fields = (
            'id',
            'alias',
            'name',
            'description',
        )
        read_only_fields = (
            'alias',
        )


class EmployeeDesignationReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeDesignation
        fields = (
            'id',
            'alias',
            'name',
            'description',
        )
        read_only_fields = (
            'alias',
        )

class OwnerUserWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'alias',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
        )
        read_only_fields = (
            'alias',
        )


class OwnerUserReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'alias',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
        )
        read_only_fields = (
            'alias',
        )


class EmployeeUserWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'alias',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'owner',
            'designation',
        )
        read_only_fields = (
            'alias',
        )


class EmployeeUserReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'alias',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
        )
        read_only_fields = (
            'alias',
        )


class CustomerUserWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'alias',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
        )
        read_only_fields = (
            'alias',
        )


class CustomerUserReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'alias',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
        )
        read_only_fields = (
            'alias',
        )
