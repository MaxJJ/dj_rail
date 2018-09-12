from rest_framework import serializers
from ..models.factura import Factura
from .person import PersonSerializer


class FacturaSerializer(serializers.ModelSerializer):
    consignee=PersonSerializer()
    consignor=PersonSerializer()
    buyer=PersonSerializer()
    seller=PersonSerializer()
    
    class Meta:
        model=Factura
        fields='__all__'

  