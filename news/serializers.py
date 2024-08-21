from rest_framework import serializers
from .models import News, Category, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags = TagSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = News
        fields = '__all__'

class UserNewsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = News
        exclude = ('is_published', 'author', 'last_modified_date',)