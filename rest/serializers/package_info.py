from rest_framework import serializers
from ..models import Package, Unit


class PackageSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = Package
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = Unit
        fields = '__all__'
