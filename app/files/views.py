from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import TagsSerializer, FileSerializer, MaterialSerializer
from .models import Tags, File, Material
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
