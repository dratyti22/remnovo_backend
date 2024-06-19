from rest_framework import serializers

from app.files.models import Tags, File, Material, ImageFile, DescriptionFile


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'user', 'section', 'name', 'parent', "time_create")
        read_only_fields = ('time_create',)


class FileSerializer(serializers.ModelSerializer):
    materials = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Material.objects.all())

    class Meta:
        model = File
        fields = ('filename', 'height', 'width', 'length', 'status', 'owners', 'materials', 'time_create')
        read_only_fields = ('time_create',)


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class ImageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFile
        fields = ["image"]


class DescriptionFileSerializer(serializers.ModelSerializer):
    image_file = ImageFileSerializer(many=True, read_only=True)
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tags.objects.all())
    file_filename = serializers.CharField()
    # user_id = serializers.ReadOnlyField(source="user.id")
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = DescriptionFile
        fields = ["pk", 'file_filename', 'user', 'title', 'description', 'line_video', 'tags',
                  'image_file', "time_create", "uploaded_images"]
        read_only_fields = ('time_create',)


    def create(self, validated_data):
        images_data = validated_data.pop("uploaded_images", None)
        tags = validated_data.pop("tags", None)
        file_name = validated_data.pop("file_filename", None)
        file = File.objects.get(filename=file_name)
        des = DescriptionFile(file=file, **validated_data)
        des.save()
        des.tags.set(tags)
        for image in images_data:
            ImageFile.objects.create(description_file=des, image=image)
        return des
