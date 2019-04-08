from rest_framework import serializers
from ..models.person import Person
from ..models.country import Country
from .country_serializer import CountrySerializer


class PersonSerializer(serializers.ModelSerializer):

    id = serializers.CharField()
    country = CountrySerializer()

    class Meta:
        model = Person
        fields = '__all__'

    def update(self, instance, validated_data):
        country_data = validated_data.pop('country')

        country_obj = Country.objects.get(pk=country_data['id'])
        country_obj.save()

        instance.__dict__.update(validated_data)

        instance.country = country_obj
        instance.save()

        return instance

    def __str__(self):
        """Unicode representation of Person."""
        return 'myrepr'
