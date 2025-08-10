from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    """
    Faqat oddiy foydalanuvchilar kirishi uchun permission.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'user'
            and not request.user.is_staff
            and not request.user.is_superuser
        )


class IsAdmin(BasePermission):
    """
    Faqat adminlar kirishi uchun permission.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'admin'
            and request.user.is_staff
            and request.user.is_superuser
        )


class IsTeacher(BasePermission):
    """
    Faqat o'qituvchilar kirishi uchun permission.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'teacher'
            and request.user.is_staff
            and not request.user.is_superuser
            and request.user.is_author
        )


class IsAuthor(BasePermission):
    """
    Faqat mualliflar (yoki adminlar) kirishi uchun permission.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_author
            and (request.user.role == 'author' or request.user.role == 'admin')
        )
