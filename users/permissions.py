from rest_framework import permissions


class ModeratorPermissions(permissions.BasePermission):
    """Класс для проверки является ли пользователь модератором"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()
