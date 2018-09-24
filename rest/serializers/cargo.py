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

        instance.description = validated_data.get('description',instance.description)
        unit_data=validated_data.pop('unit',None)
      
        unit,u_created=Unit.objects.get_or_create(**unit_data)


        
        instance.unit=unit
        package_data=validated_data.pop('package',None)
        package,p_created =Package.objects.get_or_create(**package_data)
        instance.package=package
        
        instance.save()
        print(instance.description)
        print(validated_data)
        return instance 