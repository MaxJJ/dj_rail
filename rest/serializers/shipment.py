from rest_framework import serializers
from ..models.shipment import Shipment
from ..models.container import Container
from ..models.invoice import Invoice
from ..models.railbill import Railbill
from ..models.place import Place
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
    id=serializers.CharField()
    in_station=PlaceSerializer(allow_null=True)
    out_station=PlaceSerializer(allow_null=True)

    class Meta:
        model=RoadSection
        fields='__all__'

class RailBillSerializer(serializers.ModelSerializer):
    road_sections = RoadSectionSerializer(many=True)   
    class Meta:
        model=Railbill
        fields='__all__'

    def update(self,instance,validated_data):
        road_sections=validated_data.pop('road_sections')
        road_sections_set=[]

        for section in road_sections:
            section_obj=RoadSection.objects.get(pk=section['id'])
            print(section)
            if section['in_station'] is not None:
               inst=Place.objects.get(pk=section['in_station']['id'])
               section_obj.in_station=inst
               
            if section['out_station'] is not None:
               outst=Place.objects.get(pk=section['out_station']['id'])
               section_obj.out_station=outst

            section_obj.save()
            road_sections_set.append(section_obj)
            
        instance.road_sections.set(road_sections_set)
        instance.__dict__.update(validated_data)
        instance.save()
        return instance



class ShipmentSerializer(serializers.ModelSerializer):
   
    
    container=ContainerSerializer(read_only=True)

    class Meta:
        model=Shipment
        fields='__all__'

