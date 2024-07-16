from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["customer_id", "delivery_type"]
    list_filter = ["customer_id", "delivery_type"]
