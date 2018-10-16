from rest_framework import serializers
from ..models.shipment import Shipment
from ..models.container import Container
from ..models.invoice import Invoice
from ..models.railbill import Railbill
from ..serializers.person import PersonSerializer
from ..serializers.factura import FacturaSerializer

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

class RailBillSerializer(serializers.ModelSerializer):
        
    class Meta:
        model=Railbill
        fields='__all__'

class ShipmentSerializer(serializers.ModelSerializer):

    
    container=ContainerSerializer(read_only=True)
    invoices=InvoiceSerializer(many=True,read_only=True)
    facturas=FacturaSerializer(many=True,read_only=True)
    rw_bill=RailBillSerializer(read_only=True)

    class Meta:
        model=Shipment
        fields='__all__'

