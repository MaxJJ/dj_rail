from rest_framework import serializers
from ..models.factura import Factura
from ..models.person import Person
from .person import PersonSerializer
from .cargo import CargoSerializer


class FacturaSerializer(serializers.ModelSerializer):
    consignee = PersonSerializer()
    consignor = PersonSerializer()
    buyer = PersonSerializer()
    seller = PersonSerializer()
    cargo = CargoSerializer(many=True)

    class Meta:
        model = Factura
        fields = '__all__'

    def update(self, instance, validated_data):
        consignee_data = validated_data.pop('consignee')
        consignee = Person.objects.get(pk=consignee_data['id'])
        instance.consignee = consignee

        consignor_data = validated_data.pop('consignor')
        consignor = Person.objects.get(pk=consignor_data['id'])
        instance.consignor = consignor

        buyer_data = validated_data.pop('buyer')
        buyer = Person.objects.get(pk=buyer_data['id'])
        instance.buyer = buyer

        seller_data = validated_data.pop('seller')
        seller = Person.objects.get(pk=seller_data['id'])
        instance.seller = seller

        cargo_data = validated_data.pop('cargo')
        for c in cargo_data:
            print(c)

        instance.__dict__.update(validated_data)
        instance.save()
        return instance
