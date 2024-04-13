from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import models
from profiles_api import serializers
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""
    # Sets a serializer for the APIView
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of fruits"""
        fruits = ['Banana', 'Apple', 'Orange', 'Strawberry']
        return Response({'message': 'Hello!', 'fruits': fruits})

    def post(self, request):
        """Create a hello message with our name"""
        # serializer_class is a standard class from ApiView
        # that retrives the configured Serializer that we set.
        # We are also passing the data we got from the request into the data for the serializer.
        serializer = self.serializer_class(data=request.data)

        # Django rest framework serializer can validate the input
        # Here we gonna validate that the data (name) is no longer than 10 letters.
        if serializer.is_valid():
            # Here we retrieve the validated data, in this case the name.
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        # Put is for updating an object. pk stands for the id of the object.
        # It basically replaces the object with the object provided.
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        # It will update an object but only to the field that were provided in the request.
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test api viewsets"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        random_objects = ['Waterbottle', 'Fork', 'Cup']

        return Response({'message': 'Hello!', 'random_objects': random_objects})

    def create(self, request):
        """Creates a new hello message"""
        serializer = self.serializer_class(data=request.data)

        # Django rest framework serializer can validate the input
        # Here we gonna validate that the data (name) is no longer than 10 letters.
        if serializer.is_valid():
            # Here we retrieve the validated data, in this case the name.
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # retrieve is mapped to a http GET operation, it is to GET a specific object based on pk id.
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    # update is mapped to a http PUT operation, it is PUT on the pk id.
    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    # partial_update is mapped to a http PATCH operation, it is PATCH on the pk id
    # updates the fields that were changed in the object only.
    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    # destory is mapped to a http DELETE operation, it is DELTE on the pk id.
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    # Using a ModelViewSet, it will provide us with all functions like create etc.
    # By just assigning a serializer.

    # Set up a serializer just like HelloViewSet
    serializer_class = serializers.UserProfileSerializer
    # Letting the db know which objects it should handle
    queryset = models.UserProfile.objects.all()
    # We use tokens for authentication, when user sends a request, a token will be attatched to it.
    authentication_classes = (TokenAuthentication,)
    # We set a permission for Profile viewset, so each request will be sent through UpdateOwnProfile.
    permission_classes = (permissions.UpdateOwnProfile,)
