from rest_framework import serializers
from ..models.factura import Factura
from .person import PersonSerializer
from .cargo import CargoSerializer


class FacturaSerializer(serializers.ModelSerializer):
    consignee=PersonSerializer()
    consignor=PersonSerializer()
    buyer=PersonSerializer()
    seller=PersonSerializer()
    cargo=CargoSerializer(many=True)
    
    class Meta:
        model=Factura
        fields='__all__'

  