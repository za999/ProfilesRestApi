from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of fruits"""
        fruits = ['Banana', 'Apple', 'Orange', 'Strawberry']
        return Response({'message': 'Hello!', 'fruits': fruits})
