from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Customer, Product, PriceProduct, Executor, Delivery, Order


@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ["customer_id", "delivery_type"]
    list_filter = ["customer_id", "delivery_type"]


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ["product_id", "deadlines", "delivery_terms"]
    list_filter = ["product_id"]


@admin.register(PriceProduct)
class PriceProductAdmin(ModelAdmin):
    list_display = ["price", 'currency']
    list_filter = ["price", "currency"]


admin.site.register(Executor)
admin.site.register(Delivery)
admin.site.register(Order)
