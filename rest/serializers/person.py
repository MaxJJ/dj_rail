from rest_framework import serializers
from ..models.person import Person


class PersonSerializer(serializers.ModelSerializer):

    id = serializers.CharField()
    class Meta:
        model=Person
        fields='__all__'

    def __str__(self):
        """Unicode representation of Person."""
        return 'myrepr'