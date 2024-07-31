from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from .models import OrderFreelanceModel
from .serializers import OrderFreelanceSerializers


class OrderFreelanceView(ModelViewSet):
    queryset = OrderFreelanceModel.objects.all().select_related('customer')
    serializer_class = OrderFreelanceSerializers

    filter_backends = [SearchFilter]
    search_fields = ['order', "order_type"]
