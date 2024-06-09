from django.contrib import admin

from .models import Material, File, DescriptionFile


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("filename", 'height', 'width', 'length', 'status')
    list_editable = ('height', 'width', 'length', 'status')


@admin.register(DescriptionFile)
class DescriptionFileAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'user_username', 'title']

    def file_name(self, obj):
        return obj.file.filename

    def user_username(self, obj):
        if obj.user.username:
            return f'{obj.user.username}'
