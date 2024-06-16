from django.db.models import F
from requests import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import TagsSerializer, FileSerializer, MaterialSerializer, ImageFileSerializer, \
    DescriptionFileSerializer
from .models import Tags, File, Material, ImageFile, DescriptionFile
from .permissions import TagsIsStaffOrRead, FilePermission, IsAuthorizedOrWorker


class TagsView(ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [TagsIsStaffOrRead]


class FileView(ModelViewSet):
    queryset = File.objects.all().prefetch_related("owners", 'materials')
    serializer_class = FileSerializer
    permission_classes = [FilePermission]


class MaterialView(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthorizedOrWorker]


class ImageFileView(ModelViewSet):
    queryset = ImageFile.objects.all().select_related("description_file", 'description_file__file')
    serializer_class = ImageFileSerializer


class DescriptionFileView(ModelViewSet):
    queryset = DescriptionFile.objects.all().annotate(
        tags_name=F("tags__name"),
        file_filename=F("file__filename")
    ).select_related("user", "file").prefetch_related("tags", "image_file")
    serializer_class = DescriptionFileSerializer

    def create(self, request):
        user = request.user
        file = request.data.get('file')
        title = request.data.get('title')
        description = request.data.get('description')
        line_video = request.data.get('line_video')
        tags = request.data.get('tags')
        file_name = File.objects.get(filename=file)
        tag_instances = []
        for tag in tags:
            tag_instance = Tags.objects.get(name=tag)
            tag_instances.append(tag_instance)

        description_file = DescriptionFile(file=file_name, user=user, title=title, description=description,
                                           line_video=line_video)
        description_file.save()

        for tag_instance in tag_instances:
            description_file.tags.add(tag_instance)

        image_files = request.data.get('image_file')
        if image_files:
            for image in image_files:
                try:
                    ImageFile.objects.create(image=image, description_file=description_file)
                except Exception as e:
                    print(f"Error creating ImageFile: {e}")
        else:
            print("No image files in request")

        serializer = self.serializer_class(description_file)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
