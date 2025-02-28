from rest_framework import serializers
from .models import Product
from comments.models import Comment


class ProductCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField()

class ProductCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class ProductSerializer(serializers.Serializer):
    comments = ProductCommentSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'comment')

    def create(self, validated_data):
        comments_data = validated_data.pop('comments', [])
        product = Product.objects.create(**validated_data)

        for comment_data in comments_data:
            Comment.objects.create(product=product, **comment_data)

        return product

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()
#     price = serializers.DecimalField(max_digits=12, decimal_places=2)
#     comments = ProductCommentSerializer(many=True, read_only=True)
#     category = ProductCategorySerializer(read_only=True)