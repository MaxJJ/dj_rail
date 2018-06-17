from rest_framework import serializers
from .models import Person,Order,Place,Shipment


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model=Person
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model=Order
        fields='__all__'

class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model=Place
        fields='__all__'

class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Shipment
        fields='__all__'