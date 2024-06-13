from rest_framework import serializers

from app.files.models import Tags, File, Material, ImageFile, DescriptionFile


class TagsSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tags
        fields = ('id', 'user', 'section', 'name', 'parent')


class FileSerializer(serializers.ModelSerializer):
    # owner_id = serializers.IntegerField(read_only=True)
    # materials_id = serializers.IntegerField(read_only=True)
    materials = serializers.StringRelatedField(many=True)

    class Meta:
        model = File
        fields = ('filename', 'height', 'width', 'length', 'status', 'owners', 'materials')


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class ImageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFile
        fields = ['id', 'image', 'description_file']


class DescriptionFileSerializer(serializers.ModelSerializer):
    image_file = serializers.SerializerMethodField('get_image_file')

    class Meta:
        model = DescriptionFile
        fields = ['file', 'user', 'title', 'description', 'line_video', 'tags', 'image_file']

    def get_image_file(self, obj):
        if obj.image_file.exists():
            return [img.image.url for img in obj.image_file.all()]
        else:
            return []
