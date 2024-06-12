from rest_framework import serializers

from app.files.models import Tags, File, Material


class TagsSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tags
        fields = ('id', 'user', 'section', 'name', 'parent')


class FileSerializer(serializers.ModelSerializer):
    # owner_id = serializers.IntegerField(read_only=True)
    # materials_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = File
        fields = ('filename', 'height', 'width', 'length', 'status', 'owners', 'materials')


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
