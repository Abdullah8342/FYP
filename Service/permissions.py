from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        IS_TRUE = request.user and request.user.is_authenticated
        if IS_TRUE and request.user.is_superuser:
            print('Is SuperUser')
            return True
        print("Else Condition")
        return (
            IS_TRUE
            and request.user.roll == "SP"
            and request.method in permissions.SAFE_METHODS
        )
