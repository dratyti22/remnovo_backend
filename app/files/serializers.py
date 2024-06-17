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
        fields = ["image"]


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['name']


class DescriptionFileSerializer(serializers.ModelSerializer):
    image_file = ImageFileSerializer(many=True)
    file_filename = serializers.CharField(read_only=False)
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tags.objects.all())

    class Meta:
        model = DescriptionFile
        fields = ['file_filename', 'user', 'title', 'description', 'line_video', 'tags',
                  'image_file']
