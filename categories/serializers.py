from rest_framework import serializers
from .models import Category
from products.models import Product


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    products = serializers.StringRelatedField(many=True, read_only=True)
    # products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)



    class Meta:
        model = Category
        fields = ('id', 'name', 'products', 'products_count')

    def get_products_count(self, instance):
        return instance.products.count()