from rest_framework import permissions

from common.choices import Status
from core.choices import UserKind


class IsAuthenticatedOrCreate(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super().has_permission(request, view)


class IsOwnerOrReadOnly(permissions.IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsOwner(permissions.IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsSuperUser(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_superuser)


class IsAdminUser(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return bool(request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False
        return bool(request.user and request.user.is_staff)


class CheckAnyPermission(permissions.BasePermission):

    def get_permissions(self, view):

        # Get all permissions

        _permissions = getattr(view, "available_permission_classes", [])

        if not hasattr(_permissions, "__iter__"):
            # Available_permission_classes contain only one permission
            return [_permissions]

        # Already a list
        return _permissions

    def has_permission(self, request, view):

        # Fetching all permission class name, from `available_permission_classes` variable
        _permissions = self.get_permissions(view)

        if not _permissions:
            # Does not contain any permission
            return False

        for perm_class in _permissions:

            if hasattr(perm_class, "__iter__"):
                # the current item of permissions class is iterable
                classes = perm_class
                permission_flag = False
                for _perm_class in classes:
                    # the current item of permissions class is iterable
                    permission = _perm_class()

                    if permission.has_permission(request, view):
                        permission_flag = True
                        break
                    else:
                        pass

                if permission_flag:
                    return True
            else:

                # the current item of permissions class is not iterable
                permission = perm_class()

                if permission.has_permission(request, view):
                    return True
                else:
                    pass

        return False

    def has_object_permission(self, request, view, obj):
        """
        Check the object permissions on the view.
        """

        _permissions = self.get_permissions(view)

        if not _permissions:
            return False

        for perm_class in _permissions:
            if hasattr(perm_class, "__iter__"):
                classes = perm_class

                permission_flag = False
                for _perm_class in classes:
                    permission = _perm_class()
                    if permission.has_object_permission(request, view, obj):
                        permission_flag = True
                        break
                if permission_flag:
                    return True
            else:
                permission = perm_class()

                if permission.has_object_permission(request, view, obj):
                    return True
        return False