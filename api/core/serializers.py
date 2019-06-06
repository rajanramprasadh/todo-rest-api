from rest_framework import serializers

from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for our user profile objects"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new User."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class TodoItemSerializer(serializers.ModelSerializer):
    """Serializer for Todo Items."""

    class Meta:
        model = models.TodoListItem
        fields = ('id', 'user_profile', 'todo_item', 'description', 'created_on', 'reminder_date')
        extra_kwargs = {'user_profile': {'read_only': True}}

