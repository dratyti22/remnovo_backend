from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Tags, File


class TagsIsStaffOrRead(BasePermission):
    '''
    Создавать - Сотрудники и владелец файла
    Обновлять - Сотрудники
    Удалять - Сотрудники
    Смотреть - Все, если тег является разделом.
    '''

    def has_permission(self, request, view):
        if request.method == 'POST':  # Создавать
            user_id = request.data.get('user')
            if user_id:
                user_obj = User.objects.get(id=user_id)
                if request.user == user_obj or request.user.is_staff:
                    return True
            return False
        elif request.method == 'PUT' or request.method == 'PATCH':  # Обновлять
            return request.user.is_staff
        elif request.method == 'DELETE':  # Удалять
            return request.user.is_staff
        elif request.method == 'GET':  # Смотреть
            return True
        return False


class FilePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.method == "POST":
            if request.user.is_authenticated or request.user.is_superuser:
                return True
            return False

        if request.method in ['PUT', "PATCH"]:
            file_id = request.data.get('id')
            file_obj = File.objects.get(id=file_id)
            if request.user in file_obj.owners.all() or request.user.is_staff:
                return True
            return False

        if request.method == "DELETE":
            file_id = view.kwargs.get('pk')
            print(file_id)
            file_obj = File.objects.get(id=file_id)
            if request.user in file_obj.owners.all() or request.user.is_staff:
                return True
            return False
