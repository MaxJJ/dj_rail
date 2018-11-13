from rest_framework import serializers
from ..models.place import Place

class PlaceSerializer(serializers.ModelSerializer):
    id=serializers.CharField()
    class Meta:
        model=Place
        fields='__all__'