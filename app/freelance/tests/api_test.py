import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.freelance.models import OrderFreelanceModel
from app.freelance.serializers import OrderFreelanceSerializers
from app.users.models import CustomUser


class OrderFreelanceAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='test_user', email='user1@example.com')
        self.order1 = OrderFreelanceModel.objects.create(
            order=1,
            customer=self.user,
            order_type=1,
            total_amount=100.0,
            our_model=True,
        )
        self.order2 = OrderFreelanceModel.objects.create(
            order=2,
            customer=self.user,
            order_type=2,
            total_amount=200.0,
            our_model=False,
        )

    def test_get_orders(self):
        url = reverse('orderfreelancemodel-list')
        response = self.client.get(url)
        orders = OrderFreelanceModel.objects.all()
        serializer_data = OrderFreelanceSerializers(orders, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_order(self):
        url = reverse('orderfreelancemodel-detail', args=(self.order1.id,))
        response = self.client.get(url)
        order = OrderFreelanceModel.objects.get(id=self.order1.id)
        serializer_data = OrderFreelanceSerializers(order).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create_order(self):
        url = reverse('orderfreelancemodel-list')
        data = {
            "order": 3,
            "customer": self.user.id,  # Use user ID instead of user object
            "order_type": 1,
            "total_amount": 100.0,
            "our_model": True,
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, OrderFreelanceModel.objects.all().count())

    def test_update_order(self):
        url = reverse('orderfreelancemodel-detail', args=(self.order1.id,))
        data = {
            "id": self.order1.id,
            "order": 3,
            "customer": self.user.id,  # Use user ID instead of user object
            "order_type": 2,
            "total_amount": 150.0,
            "our_model": True,
        }
        response = self.client.put(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.order1.refresh_from_db()
        self.assertEqual(150.00, self.order1.total_amount)

    def test_delete_order(self):
        url = reverse('orderfreelancemodel-detail', args=(self.order2.id,))
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, OrderFreelanceModel.objects.all().count())
