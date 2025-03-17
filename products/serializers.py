from rest_framework import serializers
from .models import Product
from comments.models import Comment


class ProductCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField()

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=12, decimal_places=2)
    comments = ProductCommentSerializer(many=True)


