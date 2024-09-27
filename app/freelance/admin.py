from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import OrderFreelanceModel


@admin.register(OrderFreelanceModel)
class OrderFreelanceAdmin(ModelAdmin):
    list_display = ["order", "order_type", "created_at"]
