from rest_framework.permissions import BasePermission
from .models import Tags


class TagsIsStaffOrRead(BasePermission):
    '''
    Создавать - Сотрудники и владелец файла
    Обновлять - Сотрудники
    Удалять - Сотрудники
    Смотреть - Все, если тег является разделом.
    '''

    def has_permission(self, request, view):
        if request.method == 'POST':  # Создавать
            user_get = request.data.get('user')
            if user_get:
                tag = Tags.objects.filter(user=user_get)
                if tag == request.user:
                    return True
            return request.user.is_staff
        elif request.method == 'PUT' or request.method == 'PATCH':  # Обновлять
            return request.user.is_staff
        elif request.method == 'DELETE':  # Удалять
            return request.user.is_staff
        elif request.method == 'GET':  # Смотреть
            return True
        return False
