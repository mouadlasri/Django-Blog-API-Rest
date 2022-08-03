# posts/serializers.py

from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model() # reference the correct user model, whether it is the default user or a customer user model
        fields = ('id', 'username',)