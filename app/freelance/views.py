from rest_framework.viewsets import ModelViewSet

from .models import OrderFreelanceModel
from .serializers import OrderFreelanceSerializers


class OrderFreelanceView(ModelViewSet):
    queryset = OrderFreelanceModel.objects.all().select_related('customer')
    serializer_class = OrderFreelanceSerializers
