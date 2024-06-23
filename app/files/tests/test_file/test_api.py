import json

from django.contrib.auth.models import User
from django.db.models import F
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.files.models import File, Material
from app.files.serializers import FileSerializer


class ApiFileSerializerTestCase(APITestCase):
    def setUp(self):
        self.material1 = Material.objects.create(name='m1', description='m1')
        self.material2 = Material.objects.create(name='m2', description='m2')
        self.material3 = Material.objects.create(name='m3', description='m3')
        self.user = User.objects.create(username='test_user1')
        self.user2 = User.objects.create(username='test_user2')

        self.file1 = File.objects.create(filename='n', height=45, width=34, length=23, status=1)
        self.file1.owners.set([self.user2])
        self.file1.materials.set([self.material1, self.material3])

        self.file2 = File.objects.create(filename='n2', height=42, width=35, length=25, status=3)
        self.file2.owners.set([self.user2, self.user])
        self.file2.materials.set([self.material1])

    def test_get(self):
        url = reverse("file-list")
        response = self.client.get(url)
        file = File.objects.all().prefetch_related("owners", 'materials')
        serializer_data = FileSerializer(file, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    # def test_get_one(self):
    #     url = reverse("File-detail", args=(self.company1.id,))
    #     response = self.client.get(url)
    #     file = File.objects.filter(id=self.company1.id).annotate(
    #         first_name=F("user__first_name"),
    #         last_name=F("user__last_name"),
    #     )
    #     serializer_data = FileSerializer(file, many=True).data
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     self.assertEqual(serializer_data, [response.data])
    #
    # def test_get_search(self):
    #     url = reverse("File-list")
    #     response = self.client.get(url, data={'search': 'test_company'})
    #     file = File.objects.filter(id__in=[self.company1.id, self.company2.id]).annotate(
    #         first_name=F("user__first_name"),
    #         last_name=F("user__last_name"),
    #     )
    #     serializer_data = FileSerializer(file, many=True).data
    #
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     self.assertEqual(serializer_data, response.data)

    def test_post(self):
        user3 = User.objects.create(username='test_user3', first_name='test_first3', last_name='test_last3')
        self.assertEqual(2, File.objects.all().count())

        url = reverse("file-list")

        data = {
            "filename": "n3",
            "height": 45.0,
            "width": 34.0,
            "length": 23.0,
            "status": 1,
            "materials": [
                self.material1.id,
                self.material3.id
            ]
        }

        json_data = json.dumps(data)
        self.client.force_login(user3)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, File.objects.all().count())

    def test_put(self):
        url = reverse("file-detail", args=(self.file1.id,))
        data = {
            'id': self.file1.id,
            "filename": "n6",
            "height": 45.0,
            "width": 34.0,
            "length": 23.0,
            "status": 1,
            "materials": [
                self.material1.id,
                self.material3.id
            ]
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user2)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.file1.refresh_from_db()
        self.assertEqual('n6', self.file1.filename)

    def test_delete(self):
        self.assertEqual(2, File.objects.all().count())

        url = reverse("file-detail", args=(self.file2.id,))
        self.client.force_login(self.user)
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, File.objects.all().count())
