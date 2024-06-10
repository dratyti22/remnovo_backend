from django.db.models import F
from rest_framework.viewsets import ModelViewSet

from .serializers import TagsSerializer
from .models import Tags
from .permissions import TagsIsStaffOrRead


class TagsView(ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [TagsIsStaffOrRead]
