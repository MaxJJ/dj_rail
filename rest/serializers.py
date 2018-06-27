from rest_framework import serializers
from .models import Person,Order,Place,Shipment


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model=Person
        fields='__all__'



class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model=Place
        fields='__all__'

class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Shipment
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    shipments=ShipmentSerializer( many=True,read_only=True)
    dispatch_place=PlaceSerializer(read_only=True)
    class Meta:
        model=Order
        fields='__all__'

class AppendShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'


  
class TstSerializer(serializers.Serializer):
    a=serializers.CharField(max_length=10)
    b=serializers.CharField(max_length=10)
    c=serializers.CharField(max_length=10)
    

