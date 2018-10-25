from rest_framework import serializers
from ..models import Cargo
from ..models.measure_unit import Unit
from ..models.package import Package
from .package_info import PackageSerializer,UnitSerializer
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
class CargoSerializer(serializers.ModelSerializer):

    package=PackageSerializer()
    unit=UnitSerializer()
    

    class Meta:
        model=Cargo
        fields='__all__'

    def update(self, instance, validated_data):

        package_data=validated_data.pop('package')
        package=Package.objects.get(pk=package_data['id'])
        unit_data=validated_data.pop('unit')
        unit=Unit.objects.get(pk=unit_data['id'])
        
        instance.package=package
        instance.unit=unit
        instance.__dict__.update(validated_data)
        
        instance.save()

        return instance 