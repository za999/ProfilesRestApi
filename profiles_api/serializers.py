from rest_framework import serializers
from profiles_api import models

# Serializer class for POST, PUT and PATCH
# Here we make sure that the max_length is 10 for any request data.
class HelloSerializer(serializers.Serializer):
    """Serializers test for ApiView"""
    name = serializers.CharField(max_length=10)

# Use meta class to configure the serializer to point to a specific model in the project
# in this case the user_profile model
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    # Serializer now points to UserProfile model
    class Meta:
        model = models.UserProfile
        # ALl the fields here will be used by the serializers
        # these are the fields we expose to the serializer from the model.
        fields = ('id', 'email', 'name', 'password')
        # Below we are setting the password field as write write_only
        # This is because so we won't return the password hash when we receive a GET reqeust.
        # We are also setting a style so the password becomes dots when typing it in the field.
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # Here we are overwriting the create function of the ModeSerializer
    # It uses the default create function of the object manager.
    # We override it, the reason we do it is because the password gets created
    # as a hash and not the default way where it gets created as simple text.

    # So whenever we create an object and the object gets provided to the
    # UserProfileSerializer, it validates each field and its contents
    # Then it will call this create function and send the validated_data in.
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    # The default update logic for ModeSerializer will take whatever fields are provided
    # in our cause email, name and password and pass them to the model.
    # But we need to actually has the password before saving it otherwise
    # we will save it in cleartext.
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            # Saves password as a hash
            instance.set_password(password)
        # Update all the remaning fields.
        return super().update(instance, validated_data)
