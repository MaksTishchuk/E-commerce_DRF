from rest_framework import serializers

from .models import Order, OrderItem

from product.serializers import ProductSerializer


class MyOrderItemSerializer(serializers.ModelSerializer):
    """ Сериализатор товара из заказов пользователя """

    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = (
            'price',
            'product',
            'quantity'
        )


class MyOrderSerializer(serializers.ModelSerializer):
    """ Сериализатор заказов пользователя """

    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'phone',
            'country',
            'city',
            'address',
            'zipcode',
            'additional_information',
            'created_at',
            'items',
            'order_price'
        )


class OrderItemSerializer(serializers.ModelSerializer):
    """ Сериализатор товара из заказа """

    class Meta:
        model = OrderItem
        fields = (
            'price',
            'product',
            'quantity'
        )


class OrderSerializer(serializers.ModelSerializer):
    """ Сериализатор заказа """

    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'phone',
            'country',
            'city',
            'address',
            'zipcode',
            'additional_information',
            'created_at',
            'items',
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order
