from rest_framework import serializers
from ..models import RtmeFileModel

class RtmeFileSerializer(serializers.ModelSerializer):

    class Meta:
        model=RtmeFileModel
        fields='__all__'