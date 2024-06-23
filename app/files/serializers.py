from rest_framework import serializers

from app.files.models import Tags, File, Material, ImageFile, DescriptionFile


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'user', 'section', 'name', 'parent', "time_create")
        read_only_fields = ('time_create', "user")


class FileSerializer(serializers.ModelSerializer):
    owners_id = serializers.SerializerMethodField("get_owners_id")

    class Meta:
        model = File
        fields = ('filename', 'height', 'width', 'length', 'status', 'owners_id', 'materials', 'time_create')
        read_only_fields = ('time_create', "owners_id")

    def get_owners_id(self, obj):
        return [owner.id for owner in obj.owners.all()]


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
    file = serializers.CharField()
    user_id = serializers.ReadOnlyField(source="user.id")
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True, required=False
    )

    class Meta:
        model = DescriptionFile
        fields = ["pk", 'file', 'user_id', 'title', 'description', 'line_video', 'tags',
                  'image_file', "time_create", "uploaded_images"]
        read_only_fields = ('time_create',)

    def create(self, validated_data):
        images_data = validated_data.pop("uploaded_images", None)
        tags = validated_data.pop("tags", None)
        file_name = validated_data.pop("file", None)
        file = File.objects.get(filename=file_name)
        des = DescriptionFile(file=file, **validated_data)
        des.save()
        des.tags.set(tags)
        if images_data:
            for image in images_data:
                ImageFile.objects.create(description_file=des, image=image)
        return des

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.line_video = validated_data.get('line_video', instance.line_video)

        if 'file' in validated_data:
            file_name = validated_data.pop("file")
            file = File.objects.get(filename=file_name)
            instance.file = file

        if 'tags' in validated_data:
            tags = validated_data.pop("tags")
            instance.tags.set(tags)

        if 'uploaded_images' in validated_data:
            images_data = validated_data.pop("uploaded_images")
            instance.image_file.all().delete()
            for image in images_data:
                ImageFile.objects.create(description_file=instance, image=image)

        instance.save()
        return instance
