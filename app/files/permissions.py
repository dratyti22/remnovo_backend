from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import File, DescriptionFile


class TagsIsStaffOrRead(BasePermission):
    '''
    Создавать - Сотрудники
    Обновлять - Сотрудники
    Удалять - Сотрудники
    Смотреть - Все
    '''

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.roles_id == 10:
            return True

        if request.method == 'POST':  # Создавать
            return request.user.roles_id == 5
        elif request.method == 'PUT' or request.method == 'PATCH':  # Обновлять
            return request.user.roles_id == 5
        elif request.method == 'DELETE':  # Удалять
            return request.user.roles_id == 5
        elif request.method == 'GET':  # Смотреть
            return True
        return False


class FilePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.roles_id == 10:
            return True

        if request.method in SAFE_METHODS:
            return True

        if request.method == "POST":
            if request.user.is_authenticated:
                return True
            return False

        if request.method in ['PUT', "PATCH"]:
            file_id = request.data.get('id')
            file_obj = File.objects.get(id=file_id)
            if request.user in file_obj.owners.all() or request.user.roles_id == 5:
                return True
            return False

        if request.method == "DELETE":
            file_id = view.kwargs.get('pk')
            file_obj = File.objects.get(id=file_id)
            if request.user in file_obj.owners.all() or request.user.roles_id == 5:
                return True
            return False


class IsAuthorizedOrWorker(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.roles_id == 10:
            return True

        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.roles_id == 5


class IsAuthorOrStaff(BasePermission):
    DANGEROUS_METHODS = ("PUT", "PATCH", "DELETE")

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.roles_id == 10:
            return True

        if request.method in SAFE_METHODS:
            return True

        elif request.method == "POST":
            return request.user.is_authenticated

        elif request.method in self.DANGEROUS_METHODS:
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.roles_id == 10:
            return True

        if request.method in SAFE_METHODS:
            return True

        elif request.method == "POST":
            return request.user in obj.file.owners.all()

        elif request.method in self.DANGEROUS_METHODS:
            file_id = view.kwargs.get('pk')
            if file_id:
                file_obj = DescriptionFile.objects.get(id=file_id)
                return request.user == file_obj.user
            return False
