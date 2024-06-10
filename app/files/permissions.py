from rest_framework.permissions import BasePermission, SAFE_METHODS


class TagsIsStaffOrRead(BasePermission):
    '''
    Создавать - Сотрудники и владелец файла
    Обновлять - Сотрудники
    Удалять - Сотрудники
    Смотреть - Все, если тег является разделом.
    '''

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return obj.section
        elif request.method == 'POST':
            return request.user.is_staff or obj.user == request.user
        else:
            return request.user.is_staff
