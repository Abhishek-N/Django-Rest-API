from rest_framework import serializers
from .models import Article
from django.utils import timezone


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']

