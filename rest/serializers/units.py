from rest_framework import serializers
from ..models.measure_unit import Unit


class UnitSerializer(serializers.ModelSerializer):
    

    class Meta:
        model=Unit
        fields='__all__'

  