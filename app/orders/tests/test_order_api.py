from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.orders.models import Customer, Product, PriceProduct, Executor, Delivery, Order
from app.orders.serializers import OrderSerializer


class OrderAPITestCase(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            customer_id=1,
            delivery_type=1,
            street="2",
            city="2",
            postal_code="32",
            delivery_deadline="fafa",
            self_pickup_hours="afsaf"
        )

        self.product = Product.objects.create(
            product_id=1,
            height=2.0,
            width=2.0,
            length=2.0,
            materials="asfa",
            deadlines="fsfa",
            delivery_terms="fasfas"
        )

        self.price_product = PriceProduct.objects.create(
            price=1223.0,
            currency="rub",
            production_cost=324.42,
            cost_delivery=32.111,
            order=False,
            margin=1000.0
        )

        self.executor = Executor.objects.create(
            executor_id=2,
            data_order_take="12fafd",
            order_execution_date="fasd",
            actual_execution_date="fasfa"
        )

        self.delivery = Delivery.objects.create(
            where_delivery="fafdasfas",
            delivery_type=2
        )

        self.order = Order.objects.create(
            customer=self.customer,
            product=self.product,
            price_product=self.price_product,
            executor=self.executor,
            delivery=self.delivery,
            status_order=4,
        )

    def test_get_orders(self):
        url = reverse("order-list")
        response = self.client.get(url)
        orders = Order.objects.all().select_related("customer", "product", "price_product", 'executor', 'delivery')
        serializer_data = OrderSerializer(orders, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_order(self):
        url = reverse("order-detail", args=(self.order.id,))
        response = self.client.get(url)
        serializer_data = OrderSerializer(self.order).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create_order(self):
        url = reverse("order-list")
        data = {
            "customer": {
                "customer_id": 1,
                "delivery_type": 1,
                "street": "2",
                "city": "2",
                "postal_code": "32",
                "delivery_deadline": "fafa",
                "self_pickup_hours": "afsaf"
            },
            "product": {
                "product_id": 1,
                "height": 2.0,
                "width": 2.0,
                "length": 2.0,
                "materials": "asfa",
                "deadlines": "fsfa",
                "delivery_terms": "fasfas"
            },
            "price_product": {
                "price": 1223.0,
                "currency": "rub",
                "production_cost": 324.42,
                "cost_delivery": 32.111,
                "order": False,
                "margin": 1000.0
            },
            "executor": {
                "executor_id": 2,
                "data_order_take": "12fafd",
                "order_execution_date": "fasd",
                "actual_execution_date": "fasfa"
            },
            "delivery": {
                "where_delivery": "fafdasfas",
                "delivery_type": 2
            },
            "status_order": 4,
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(2, Order.objects.all().count())

    def test_update_order(self):
        url = reverse("order-detail", args=(self.order.id,))
        data = {
            "customer": {
                "customer_id": self.customer.customer_id,
                "delivery_type": self.customer.delivery_type,
                "street": self.customer.street,
                "city": self.customer.city,
                "postal_code": self.customer.postal_code,
                "delivery_deadline": self.customer.delivery_deadline,
                "self_pickup_hours": self.customer.self_pickup_hours
            },
            "product": {
                "product_id": self.product.product_id,
                "height": self.product.height,
                "width": self.product.width,
                "length": self.product.length,
                "materials": self.product.materials,
                "deadlines": self.product.deadlines,
                "delivery_terms": self.product.delivery_terms
            },
            "price_product": {
                "price": self.price_product.price,
                "currency": self.price_product.currency,
                "production_cost": self.price_product.production_cost,
                "cost_delivery": self.price_product.cost_delivery,
                "order": self.price_product.order,
                "margin": self.price_product.margin
            },
            "executor": {
                "executor_id": self.executor.executor_id,
                "data_order_take": self.executor.data_order_take,
                "order_execution_date": self.executor.order_execution_date,
                "actual_execution_date": self.executor.actual_execution_date
            },
            "delivery": {
                "where_delivery": self.delivery.where_delivery,
                "delivery_type": self.delivery.delivery_type
            },
            "status_order": 5,
        }
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.order.refresh_from_db()
        self.assertEqual('5', self.order.status_order)

    def test_delete_order(self):
        url = reverse("order-detail", args=(self.order.id,))
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(0, Order.objects.all().count())
