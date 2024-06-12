from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import TagsSerializer, FileSerializer
from .models import Tags, File
from .permissions import TagsIsStaffOrRead, FilePermission


class TagsView(ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [TagsIsStaffOrRead]


class FileView(ModelViewSet):
    queryset = File.objects.all().prefetch_related("owners", 'materials')
    serializer_class = FileSerializer
    permission_classes = [FilePermission]

