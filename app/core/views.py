from django.shortcuts import render

from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from . import models, serializers, permissions

# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', 'username',)


class LoginViewSet(viewsets.ViewSet):
    """Checks Email and password and returns auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the obtain auth token API view to validate and create a token."""

        return ObtainAuthToken().post(request)


class TodoListViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, and updating todo list items."""

    serializer_class = serializers.TodoListSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = models.TodoList.objects.all()
    permission_classes = (permissions.PostTodoList, IsAuthenticated)

    def perform_create(self, serializer):
        """Set the user profile to the logged user."""

        serializer.save(user_profile=self.request.user)
