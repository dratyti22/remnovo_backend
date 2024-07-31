from rest_framework import serializers

from app.freelance.models import OrderFreelanceModel


class OrderFreelanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderFreelanceModel
        fields = "__all__"
