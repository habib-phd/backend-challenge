from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # If the request method is one of the safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            # Allow read-only permissions
            return True
        # Check if the object's owner is the same as the current user making the request
        return obj.owner == request.user
