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


class DescriptionFileSerializer(serializers.ModelSerializer):
    image_file = ImageFileSerializer(many=True)
    tags_name = serializers.ListField(child=serializers.CharField(), write_only=True)
    tags_name_display = serializers.SerializerMethodField()
    file_filename = serializers.CharField(read_only=False)

    class Meta:
        model = DescriptionFile
        fields = ['file_filename', 'user', 'title', 'description', 'line_video', 'tags_name', 'tags_name_display',
                  'image_file']

    def get_tags_name_display(self, obj):
        return [tag.name for tag in obj.tags.all()]
