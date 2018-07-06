from rest_framework import serializers
from ..models.shipment import Shipment

class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Shipment
        fields='__all__'