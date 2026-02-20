from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        print('IsAdminOrReadOnly')
        try:
            print('try')
            print(request.user.is_superuser)
            if request.method in permissions.SAFE_METHODS:
                return True
            return request.user.is_superuser
        except Exception:
            print('exception')
            if request.method in permissions.SAFE_METHODS:
                return True
