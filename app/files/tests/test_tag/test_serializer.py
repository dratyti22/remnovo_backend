from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from app.files.models import Tags
from app.files.serializers import TagsSerializer


class ProductSerializersTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user1')
        self.user2 = User.objects.create(username='test_user2')

        self.tag1 = Tags.objects.create(user=self.user2, name='tag2', section=True)
        self.tag2 = Tags.objects.create(user=self.user, name='tag3', section=True, parent=self.tag1)

        self.tag_test = Tags.objects.filter(section=True)

    def test_ok(self):
        data = TagsSerializer(self.tag_test, many=True).data
        expect_data = [
            {
                "id": self.tag1.id,
                "user": self.user2.id,
                "section": True,
                "name": "tag2",
                "parent": None
            },
            {
                "id": self.tag2.id,
                "user": self.user.id,
                "section": True,
                "name": "tag3",
                "parent": self.tag1.id
            },
        ]

        self.assertEqual(expect_data, data)
