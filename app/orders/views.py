from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from app.orders.models import Order
from app.orders.serializers import OrderSerializer


class OrderView(ModelViewSet):
    queryset = Order.objects.all().select_related("customer", "product", "price_product", 'executor', 'delivery')
    serializer_class = OrderSerializer
