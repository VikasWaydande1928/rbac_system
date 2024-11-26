# users/permissions.py
from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'Admin'


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'Moderator'


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'User'
