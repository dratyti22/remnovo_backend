from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Material, File, DescriptionFile, ImageFile, Tags

from mptt.admin import DraggableMPTTAdmin


@admin.register(Material)
class MaterialAdmin(ModelAdmin):
    pass


@admin.register(File)
class FileAdmin(ModelAdmin):
    list_display = ("filename", 'height', 'width', 'length', 'status')
    list_editable = ('height', 'width', 'length', 'status')


@admin.register(DescriptionFile)
class DescriptionFileAdmin(ModelAdmin):
    list_display = ['file_name', 'user_username', 'title']

    def file_name(self, obj):
        return obj.file.filename

    def user_username(self, obj):
        if obj.user.username:
            return f'{obj.user.username}'


@admin.register(ImageFile)
class ImageFileAdmin(ModelAdmin):
    list_display = ['description_file', 'image']

    def description_file(self, obj):
        return obj.description_file.title


@admin.register(Tags)
class TagsAdmin(DraggableMPTTAdmin):
    list_display = ("tree_actions", "indented_title", 'id', 'name', 'display_user', 'section')
    list_display_links = ('name',)
    list_filter = ('user', 'section')
    search_fields = ('name',)

    def display_user(self, obj):
        if obj.user.username:
            return obj.user.username
