from django.contrib import admin

from .models import Material, File


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("filename", 'height', 'width', 'length', 'status')
    list_editable = ('height', 'width', 'length', 'status')
