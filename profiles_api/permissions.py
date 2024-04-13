from rest_framework import permissions

# This is a custom class that will handle the permission of allowing to change the values
# of a specific field for a specific Model.

# This custom permission class will call ___ each time a request is being made
# for the specific API this class will be assigned to.

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    # So below we're going to check if we're going to let
    # a specific reqeust to be able to make a change on the actual obj.
    def has_object_permission(self, request, view, obj):
        """Checks if the user is trying to update their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
