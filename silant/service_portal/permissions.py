from rest_framework import permissions

class IsManagerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='managers').exists()

class IsServiceUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='service').exists()
