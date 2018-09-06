from rest_framework import serializers
from ..models import Cargo
from ..models.measure_unit import Unit
from .package_info import PackageSerializer,UnitSerializer
class CargoSerializer(serializers.ModelSerializer):

    package=PackageSerializer(read_only=True)
    unit=UnitSerializer(read_only=True)

    class Meta:
        model=Cargo
        fields='__all__'

    # def update(self, instance, validated_data):
       
    #     instance.__dict__.update(validated_data)
    #     instance.unit = validated_data.get('unit')
    #     # instance.unit.save()
    #     instance.save()
    #     print(instance.unit.__dict__)
        
    #     return instance 