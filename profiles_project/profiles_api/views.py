from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models
from profiles_api import permissions


class HelloAPIView(APIView):
    """Test API View"""

    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as function (get,post ,patch,put delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over you application logic",
            "Is mapped manually to URLs",
        ]
        return Response({"message": "Hello!", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializers = self.serializers_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get("name")
            message = f"hello {name}"
            return Response({"message": message})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating object"""
        return Response({"Method": "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"Method": "Patch"})

    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({"Method": "delete"})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializers_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello Message"""
        a_viewset = [
            "Uses Actions (list, create, retrieve,update,partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code",
        ]
        return Response({"message": "Hello!", "a_viewset": a_viewset})

    def create(self, request):
        "Create a new hello message"
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieve getting an object by its ID"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """handle updating an object"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({"http_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializers
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
