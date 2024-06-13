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
    queryset = DescriptionFile.objects.all().select_related("user", "file").prefetch_related("tags", "image_file")
    serializer_class = DescriptionFileSerializer
