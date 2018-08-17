from rest_framework import serializers
from ..models import Cargo
from .package_info import PackageSerializer,UnitSerializer
class CargoSerializer(serializers.ModelSerializer):

    package=PackageSerializer()
    unit=UnitSerializer()

    class Meta:
        model=Cargo
        fields='__all__'
