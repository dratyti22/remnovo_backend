from .models import CustomUser

from django.contrib import admin


# admin.site.register(User)


@admin.register(CustomUser)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['username', 'roles_id']
    search_fields = ["username", "last_name", 'first_name']
