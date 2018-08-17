from rest_framework import serializers
from ..models.order import Order
from ..models.place import Place
from .shipment import ShipmentSerializer
from .place import PlaceSerializer
from .cargo import CargoSerializer
from .person import PersonSerializer

class OrderSerializer(serializers.ModelSerializer):
    shipments=ShipmentSerializer( many=True,read_only=True)
    inbound_cargo=CargoSerializer(many=True,read_only=True)
    dispatch_place=PlaceSerializer(read_only=True)
    destination_place=PlaceSerializer(read_only=True)
    will_arrive=serializers.DateField(format="%d-%m-%Y",input_formats=['%d-%m-%Y',])
    consignor=PersonSerializer(read_only=True)
    consignee=PersonSerializer(read_only=True)
    

    class Meta:
        model=Order
        fields='__all__'

