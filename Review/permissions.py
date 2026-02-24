from rest_framework import permissions

class IsOwnerOrIsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print('IsOwnerOrIsAdminOrRradOnly')
        print(f"Request.User -: {request.user}")
        print(f"Request.User.Is_Superuser -: {request.user.is_superuser}")
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user or request.user.is_superuser
