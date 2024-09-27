from .models import CustomUser
from unfold.admin import ModelAdmin
from django.contrib import admin


# admin.site.register(User)


@admin.register(CustomUser)
class CategoriesAdmin(ModelAdmin):
    list_display = ['username', 'roles_id']
    search_fields = ["username", "last_name", 'first_name']
