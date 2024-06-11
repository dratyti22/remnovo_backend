from rest_framework.permissions import BasePermission, SAFE_METHODS


class TagsIsStaffOrRead(BasePermission):
    '''
    Создавать - Сотрудники и владелец файла
    Обновлять - Сотрудники
    Удалять - Сотрудники
    Смотреть - Все, если тег является разделом.
    '''

    DANGEROUS_METHODS = ("PUT", "PATCH", "DELETE")

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in self.DANGEROUS_METHODS and request.user.is_authenticated and request.user.is_staff or
            request.method == "POST" and request.user.is_authenticated and (
                    request.user.is_staff or obj.user == request.user)
        )
