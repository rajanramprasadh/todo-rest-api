from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostTodoList(permissions.BasePermission):
    """Allow user to update their Todo List."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update their own Todo List"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile_id == request.user.id
