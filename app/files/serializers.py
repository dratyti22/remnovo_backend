from rest_framework import serializers

from app.files.models import Tags


class TagsSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tags
        fields = ('id', 'user', 'section', 'name', 'parent')
