from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'display_name',
                  'profile_picture', 'bio', 'verified', 'posts_count']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'caption', 'image', 'created_at', 'user']
        extra_kwargs = {
            'user': {'read_only': True}
        }