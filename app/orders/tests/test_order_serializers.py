from app.users.models import CustomUser
from django.db.models import F
from rest_framework.test import APITestCase

from app.orders.models import Customer, Product, PriceProduct, Executor, Delivery, Order
from app.orders.serializers import OrderSerializer


class ProductSerializersTestCase(APITestCase):
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

        self.order_test = Order.objects.all().select_related(
            "customer", "product", "price_product", 'executor',
            'delivery'
        )

    def test_ok(self):
        data = OrderSerializer(self.order_test, many=True).data
        expect_data = [
            {
                "id": self.order.id,
                "customer": {
                    "id": self.customer.id,
                    "customer_id": 1,
                    "delivery_type": 1,
                    "street": "2",
                    "city": "2",
                    "postal_code": "32",
                    "delivery_deadline": "fafa",
                    "self_pickup_hours": "afsaf"
                },
                "product": {
                    "id": self.product.id,
                    "product_id": 1,
                    "height": 2.0,
                    "width": 2.0,
                    "length": 2.0,
                    "materials": "asfa",
                    "deadlines": "fsfa",
                    "delivery_terms": "fasfas"
                },
                "price_product": {
                    "id": self.price_product.id,
                    "price": 1223.0,
                    "currency": "rub",
                    "production_cost": 324.42,
                    "cost_delivery": 32.111,
                    "order": False,
                    "margin": 1000.0
                },
                "executor": {
                    "id": self.executor.id,
                    "executor_id": 2,
                    "data_order_take": "12fafd",
                    "order_execution_date": "fasd",
                    "actual_execution_date": "fasfa"
                },
                "delivery": {
                    "id": self.delivery.id,
                    "where_delivery": "fafdasfas",
                    "delivery_type": "2"
                },
                "status_order": "4"
            }
        ]

        self.assertEqual(expect_data, data)
