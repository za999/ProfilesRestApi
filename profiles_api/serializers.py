from rest_framework import serializers

# Serializer class for POST, PUT and PATCH
# Here we make sure that the max_length is 10 for any request data.
class HelloSerializer(serializers.Serializer):
    """Serializers test for ApiView"""
    name = serializers.CharField(max_length=10)
