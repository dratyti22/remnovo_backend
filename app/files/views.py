from django.db.models import F
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .serializers import TagsSerializer, FileSerializer, MaterialSerializer, ImageFileSerializer, \
    DescriptionFileSerializer
from .models import Tags, File, Material, ImageFile, DescriptionFile
from .permissions import TagsIsStaffOrRead, FilePermission, IsAuthorizedOrWorker


class TagsView(ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [TagsIsStaffOrRead]
    filter_backends = [SearchFilter]
    search_fields = ['name', "user__id"]


class FileView(ModelViewSet):
    queryset = File.objects.all().prefetch_related("owners", 'materials')
    serializer_class = FileSerializer
    permission_classes = [FilePermission]
    filter_backends = [SearchFilter]
    search_fields = ['status', "time_create", "owners__id"]


class MaterialView(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthorizedOrWorker]


class ImageFileView(ModelViewSet):
    queryset = ImageFile.objects.all().select_related("description_file", 'description_file__file')
    serializer_class = ImageFileSerializer


class DescriptionFileView(ModelViewSet):
    queryset = DescriptionFile.objects.all().annotate(
        file_filename=F("file__filename")
    ).select_related("user").prefetch_related("tags", "image_file")
    serializer_class = DescriptionFileSerializer
    filter_backends = [SearchFilter]
    search_fields = ["time_create", "user__id", "tags__name"]
