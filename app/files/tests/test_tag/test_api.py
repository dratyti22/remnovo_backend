import json

from django.contrib.auth.models import User
from django.db.models import F
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.files.models import Tags
from app.files.serializers import TagsSerializer


class ApiTagsSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user1')
        self.user2 = User.objects.create(username='test_user2')

        self.tag1 = Tags.objects.create(user=self.user2, name='tag2', section=True)
        self.tag2 = Tags.objects.create(user=self.user, name='tag3', section=True, parent=self.tag1)

    def test_get(self):
        url = reverse("tags-list")
        response = self.client.get(url)
        tag = Tags.objects.filter(section=True)
        serializer_data = TagsSerializer(tag, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    # def test_get_one(self):
    #     url = reverse("Tags-detail", args=(self.company1.id,))
    #     response = self.client.get(url)
    #     tag = Tags.objects.filter(id=self.company1.id).annotate(
    #         first_name=F("user__first_name"),
    #         last_name=F("user__last_name"),
    #     )
    #     serializer_data = TagsSerializer(tag, many=True).data
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     self.assertEqual(serializer_data, [response.data])
    #
    # def test_get_search(self):
    #     url = reverse("tags-list")
    #     response = self.client.get(url, data={'search': 'test_company'})
    #     tag = Tags.objects.filter(id__in=[self.company1.id, self.company2.id]).annotate(
    #         first_name=F("user__first_name"),
    #         last_name=F("user__last_name"),
    #     )
    #     serializer_data = TagsSerializer(tag, many=True).data
    #
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     self.assertEqual(serializer_data, response.data)

    def test_post(self):
        user3 = User.objects.create(username='test_user3', first_name='test_first3', last_name='test_last3')
        self.assertEqual(2, Tags.objects.all().count())

        url = reverse("tags-list")

        data = {
            "user": user3.id,
            "section": True,
            "name": "a",
            "parent": None,
        }

        json_data = json.dumps(data)
        # self.client.force_login(user3)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Tags.objects.all().count())

    def test_put(self):
        url = reverse("Tags-detail", args=(self.company1.id,))
        data = {
            'id': self.t.id,
            "name": 'name',
            "address": 'addr',
            "email": 'test@gmail.com3',
            "phone": 'test_phone3',
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.company1.refresh_from_db()
        self.assertEqual('name', self.company1.name)

    def test_delete(self):
        self.assertEqual(2, Tags.objects.all().count())

        url = reverse("Tags-detail", args=(self.company1.id,))
        self.client.force_login(self.user)
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, Tags.objects.all().count())
