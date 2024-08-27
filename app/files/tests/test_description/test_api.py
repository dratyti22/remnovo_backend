import json

from app.users.models import CustomUser
from django.db.models import F
from django.test import RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.files.models import File, Material, Tags, DescriptionFile, ImageFile
from app.files.serializers import FileSerializer, DescriptionFileSerializer


class ApiFileSerializerTestCase(APITestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create(email='user1@example.com', username='user1', roles_id=0)
        self.user2 = CustomUser.objects.create(email='user2@example.com', username='user2', roles_id=0)

        self.tag1 = Tags.objects.create(user=self.user2, name='tag2', section=True, time_create=1718613878)
        self.tag2 = Tags.objects.create(user=self.user1, name='tag3', section=True, parent=self.tag1,
                                        time_create=1718613878)

        self.material1 = Material.objects.create(name='m1', description='m1')
        self.material2 = Material.objects.create(name='m2', description='m2')
        self.material3 = Material.objects.create(name='m3', description='m3')

        self.file1 = File.objects.create(filename='n', height=45, width=34, length=23, status=1, time_create=1718614129)
        self.file1.owners.set([self.user2])
        self.file1.materials.set([self.material1, self.material3])
        self.file2 = File.objects.create(filename='n2', height=42, width=35, length=25, status=3,
                                         time_create=1718614129)
        self.file2.owners.set([self.user2, self.user1])
        self.file2.materials.set([self.material1])

        self.des1 = DescriptionFile.objects.create(
            file=self.file1,
            user=self.user1,
            title="nnn",
            description="nnn",
            line_video="https://yootube.com/nnn",
            time_create=1718613657
        )
        self.des1.tags.set([self.tag1])

        self.des2 = DescriptionFile.objects.create(
            file=self.file2,
            user=self.user2,
            title="ффф",
            description="фффффффф",
            line_video="https://yootube.com/afal",
            time_create=1718613657
        )
        self.des2.tags.set([self.tag1, self.tag2])

        self.foto1 = ImageFile.objects.create(description_file=self.des1,
                                              image="among-us-space-background-4k-wallpaper-uhdpaper.com-9230f.jpg")

    def test_get(self):
        url = reverse("descriptionfile-list")
        response = self.client.get(url)
        file = DescriptionFile.objects.all().annotate(
            file_filename=F("file__filename")
        ).select_related("user").prefetch_related("tags", "image_file")
        factory = RequestFactory()
        request = factory.get(url)
        serializer_data = DescriptionFileSerializer(file, many=True, context={'request': request}).data
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
        self.assertEqual(2, DescriptionFile.objects.all().count())

        url = reverse("descriptionfile-list")
        data = {
            "file": self.file1.filename,
            "title": "aaa",
            "description": "aaa",
            "line_video": "https://yootube.com/aaa",
            "tags": [
                self.tag1.id,
                self.tag2.id
            ],
            "uploaded_images": []
        }
        self.client.force_login(self.user1)
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, DescriptionFile.objects.all().count())

    def test_put(self):
        url = reverse("descriptionfile-detail", args=(self.des2.id,))
        data = {
            'id': self.des2.id,
            "title": "fff",
            "file": self.file2.filename,
            "description": "фффффффф",
            "line_video": "https://yootube.com/afal",
            "time_create": 1718613657,
            "tags": [self.tag1.id, self.tag2.id]
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user2)
        response = self.client.put(url, data=json_data, content_type="application/json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.des2.refresh_from_db()
        self.assertEqual('fff', self.des2.title)

    def test_delete(self):
        self.assertEqual(2, DescriptionFile.objects.all().count())

        url = reverse("descriptionfile-detail", args=(self.des2.id,))
        self.client.force_login(self.user2)
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, DescriptionFile.objects.all().count())

    def test_get_one(self):
        url = reverse("descriptionfile-detail", args=(self.des1.id,))
        response = self.client.get(url)
        file = DescriptionFile.objects.get(id=self.des1.id)
        serializer = DescriptionFileSerializer(file, context={'request': response.wsgi_request})
        serializer_data = serializer.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse("descriptionfile-list")
        response = self.client.get(url, data={'search': 'nnn'})
        file = DescriptionFile.objects.filter(tags__name='nnn')
        serializer = DescriptionFileSerializer(file, many=True, context={'request': response.wsgi_request})
        serializer_data = serializer.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_put_unauthorized(self):
        url = reverse("descriptionfile-detail", args=(self.des2.id,))
        data = {
            'id': self.des2.id,
            "title": "fff",
            "file": self.file2.filename,
            "description": "фффффффф",
            "line_video": "https://yootube.com/afal",
            "time_create": 1718613657,
            "tags": [self.tag1.name, self.tag2.name]
        }
        json_data = json.dumps(data)
        response = self.client.put(url, data=json_data, content_type="application/json")
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_delete_unauthorized(self):
        url = reverse("descriptionfile-detail", args=(self.des2.id,))
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
