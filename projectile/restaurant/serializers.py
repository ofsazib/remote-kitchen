from rest_framework import serializers
from restaurant.models import (
    Restaurant,
    Menu,
    MenuItem,
    Order,
    OrderItem,
)

class RestaurantWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = (
            'id',
            'alias',
            'name',
            'description',
            'address',
        )
        read_only_fields = (
            'alias',
        )


class RestaurantReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = (
            'id',
            'alias',
            'name',
            'description',
            'address',
        )
        read_only_fields = (
            'alias',
        )


class MenuWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = (
            'id',
            'alias',
            'name',
            'description',
            'restaurant',
        )
        read_only_fields = (
            'alias',
        )


class MenuReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = (
            'id',
            'alias',
            'name',
            'description',
            'restaurant',
        )
        read_only_fields = (
            'alias',
        )


class MenuItemWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = (
            'id',
            'alias',
            'name',
            'description',
            'menu',
            'price',
        )
        read_only_fields = (
            'alias',
        )


class MenuItemReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = (
            'id',
            'alias',
            'name',
            'description',
            'menu',
            'price',
        )
        read_only_fields = (
            'alias',
        )
