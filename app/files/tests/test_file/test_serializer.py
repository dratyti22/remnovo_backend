from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from app.files.models import File, Material
from app.files.serializers import FileSerializer


class ProductSerializersTestCase(APITestCase):
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

        self.file_test = File.objects.all().prefetch_related("owners", 'materials').order_by('id')

    def test_ok(self):
        data = FileSerializer(self.file_test, many=True).data
        expect_data = [
            {
                "filename": "n",
                "height": 45.0,
                "width": 34.0,
                "length": 23.0,
                "status": 1,
                "owners": [
                    self.user2.id
                ],
                "materials": [
                    self.material1.id,
                    self.material3.id
                ]
            },
            {
                "filename": "n2",
                "height": 42.0,
                "width": 35.0,
                "length": 25.0,
                "status": 3,
                "owners": [
                    self.user.id,
                    self.user2.id,
                ],
                "materials": [
                    self.material1.id,
                ]
            },
        ]

        self.assertEqual(expect_data, data)
