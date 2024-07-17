from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from app.orders.models import Order
from app.orders.serializers import OrderSerializer


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
