from rest_framework import serializers

from ..models.country import Country


class CountrySerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Country
        fields = '__all__'

    def __str__(self):
        """Unicode representation of Person."""
        return 'myrepr'
