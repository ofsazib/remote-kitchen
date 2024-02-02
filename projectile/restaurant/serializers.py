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


class OrderItemWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = (
            'id',
            # 'alias',
            'menu_item',
            'quantity',
        )
        read_only_fields = (
            # 'alias',
        )


class OrderReadSerializer(serializers.ModelSerializer):
    items = MenuItemReadSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'alias',
            'user',
            'items',
            'total_price',
            'created_at',
        )
        read_only_fields = (
            'alias',
        )

class OrderPayloadSerializer(serializers.ModelSerializer):
    items = OrderItemWriteSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'items',
        )
        read_only_fields = ()

    def create(self, validated_data):
        items = validated_data.pop('items')
        total_price = 0
        item_data = []
        for item in items:
            menu_item = item.get("menu_item")
            total_price += menu_item.price * item.get("quantity")
        order = Order.objects.create(user=self.context.get('request').user, total_price=total_price)
        for item in items:
            item_data.append(
                OrderItem(
                    order=order,
                    menu_item=item.get("menu_item"),
                    quantity=item.get("quantity")
                )
            )
        created_items = OrderItem.objects.bulk_create(item_data)
        return created_items
