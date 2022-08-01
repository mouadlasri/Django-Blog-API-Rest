# posts/serializers.py

from rest_framework import serializer
from .models import Post

class PostSerializer(serializer.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at')