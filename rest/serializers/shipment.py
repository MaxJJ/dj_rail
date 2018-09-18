from rest_framework import serializers
from ..models.shipment import Shipment
from ..models.container import Container
from ..models.invoice import Invoice
from ..serializers import PersonSerializer

class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model=Invoice
        fields='__all__'

class ContainerSerializer(serializers.ModelSerializer):

    class Meta:
        model=Container
        fields='__all__'

class ShipmentSerializer(serializers.ModelSerializer):

    seller= PersonSerializer()
    buyer = PersonSerializer()
    container=ContainerSerializer()
    invoices=InvoiceSerializer()

    class Meta:
        model=Shipment
        fields='__all__'

  