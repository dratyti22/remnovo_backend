from app.users.models import CustomUser
from django.db.models import F
from rest_framework.test import APITestCase

from app.files.models import DescriptionFile, File, Material, Tags, ImageFile
from app.files.serializers import DescriptionFileSerializer


class ProductSerializersTestCase(APITestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create(username='user1',email='user1@example.com')
        self.user2 = CustomUser.objects.create(username='user2',email='user2@example.com')

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
                                              image="http://localhost:8000/media/file_image/among-us-space-background-4k-wallpaper-uhdpaper.com-9230f.jpg")

        self.file_test = DescriptionFile.objects.all().annotate(
            file_filename=F("file__filename")
        ).select_related("user").prefetch_related("tags", "image_file").order_by("id")

    def test_ok(self):
        data = DescriptionFileSerializer(self.file_test, many=True).data
        expect_data = [
            {
                "pk": self.des1.pk,
                "file": "n",
                "user_id": self.user1.id,
                "title": "nnn",
                "description": "nnn",
                "line_video": "https://yootube.com/nnn",
                "tags": [
                    self.tag1.id
                ],
                "image_file": [
                    {
                        "image": "/media/http%3A/localhost%3A8000/media/file_image/among-us-space-background-4k-wallpaper-uhdpaper.com-9230f.jpg"
                    }
                ],
                "time_create": 1718613657
            },
            {
                "pk": self.des2.pk,
                "file": "n2",
                "user_id": self.user2.id,
                "title": "ффф",
                "description": "фффффффф",
                "line_video": "https://yootube.com/afal",
                "tags": [
                    self.tag1.id,
                    self.tag2.id
                ],
                "image_file": [
                ],
                "time_create": 1718613657
            },
        ]

        self.assertEqual(expect_data, data)
