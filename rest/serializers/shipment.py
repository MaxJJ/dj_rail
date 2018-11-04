from rest_framework import serializers
from ..models.shipment import Shipment
from ..models.container import Container
from ..models.invoice import Invoice
from ..models.railbill import Railbill
from ..models.road_section import RoadSection
from ..serializers.person import PersonSerializer
from ..serializers.factura import FacturaSerializer
from ..serializers.place import PlaceSerializer

class InvoiceSerializer(serializers.ModelSerializer):
    seller= PersonSerializer()
    buyer = PersonSerializer()
    class Meta:
        model=Invoice
        fields='__all__'

class ContainerSerializer(serializers.ModelSerializer):

    class Meta:
        model=Container
        fields='__all__'

class RoadSectionSerializer(serializers.ModelSerializer):

    in_station=PlaceSerializer()
    out_station=PlaceSerializer()

    class Meta:
        model=RoadSection
        fields='__all__'

class RailBillSerializer(serializers.ModelSerializer):
    road_sections = RoadSectionSerializer(many=True,read_only=True)   
    class Meta:
        model=Railbill
        fields='__all__'



class ShipmentSerializer(serializers.ModelSerializer):
   
    
    container=ContainerSerializer(read_only=True)

    class Meta:
        model=Shipment
        fields='__all__'

