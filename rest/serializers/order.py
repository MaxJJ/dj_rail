from rest_framework import serializers
from ..models.order import Order
from .shipment import ShipmentSerializer
from .place import PlaceSerializer

class OrderSerializer(serializers.ModelSerializer):
    shipments=ShipmentSerializer( many=True,read_only=True)
    dispatch_place=PlaceSerializer(read_only=True)
    will_arrive=serializers.DateField(format="%d-%m-%Y",input_formats=['%d-%m-%Y',])
    class Meta:
        model=Order
        fields='__all__'