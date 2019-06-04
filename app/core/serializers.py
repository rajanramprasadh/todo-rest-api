from rest_framework import serializers

from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for our user profile objects"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'first_name',
                  'last_name', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class TodoListSerializer(serializers.ModelSerializer):
    """Serializer for Todo List items."""

    class Meta:
        model = models.TodoList
        fields = ('id', 'user_profile', 'todo_text')
        extra_kwargs = {'user_profile': {'read_only': True}}
