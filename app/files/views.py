from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import TagsSerializer
from .models import Tags
from .permissions import TagsIsStaffOrRead


class TagsView(ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [TagsIsStaffOrRead]


# class TagGetView(ListAPIView, GenericAPIView):
#     queryset = Tags.objects.all()
#     serializer_class = TagsSerializer
#     permission_classes = []
