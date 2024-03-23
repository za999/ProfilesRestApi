from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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
