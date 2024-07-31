from django.contrib import admin

from .models import OrderFreelanceModel


@admin.register(OrderFreelanceModel)
class OrderFreelanceAdmin(admin.ModelAdmin):
    list_display = ["order", "order_type", "created_at"]
