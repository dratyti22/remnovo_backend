from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from app.files.models import Tags
from app.files.serializers import TagsSerializer
from app.users.models import CustomUser


class ProductSerializersTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='test_user1', email='user1@example.com')
        self.user2 = CustomUser.objects.create(username='test_user2', email='user12@example.com')

        self.tag1 = Tags.objects.create(user=self.user2, name='tag2', section=True, time_create=1718613878)
        self.tag2 = Tags.objects.create(user=self.user, name='tag3', section=True, parent=self.tag1,
                                        time_create=1718613878)

        self.tag_test = Tags.objects.filter(section=True)

    def test_ok(self):
        data = TagsSerializer(self.tag_test, many=True).data
        expect_data = [
            {
                "id": self.tag1.id,
                "user": self.user2.id,
                "section": True,
                "name": "tag2",
                "parent": None,
                'time_create': 1718613878
            },
            {
                "id": self.tag2.id,
                "user": self.user.id,
                "section": True,
                "name": "tag3",
                "parent": self.tag1.id,
                'time_create': 1718613878
            },
        ]

        self.assertEqual(expect_data, data)
