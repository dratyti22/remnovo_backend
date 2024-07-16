from django.contrib import admin

from .models import Customer, Product


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["customer_id", "delivery_type"]
    list_filter = ["customer_id", "delivery_type"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_id", "deadlines", "delivery_terms"]
    list_filter = ["product_id"]
