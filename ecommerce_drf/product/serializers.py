from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """ Сериализатор для категорий в товаре """

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'get_image')


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор товаров """

    category = CategorySerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'description',
            'price',
            'discount_price',
            'get_absolute_url',
            'get_image',
            'get_thumbnail',
        )


class CategoryProductsSerializer(serializers.ModelSerializer):
    """ Сериализатор для вывода информации о категории и всех товарах в ней """

    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'products', 'get_image', 'get_absolute_url')
