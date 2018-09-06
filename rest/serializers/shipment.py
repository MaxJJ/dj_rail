from rest_framework import serializers
from ..models.shipment import Shipment
from ..serializers import PersonSerializer

class ShipmentSerializer(serializers.ModelSerializer):

    seller= PersonSerializer()
    buyer = PersonSerializer()

    class Meta:
        model=Shipment
        fields='__all__'

  