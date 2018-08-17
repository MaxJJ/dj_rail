from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.cargo import CargoSerializer
from ..models.cargo import Cargo


class NewCargo(APIView):
    """ Get new created Cargo.
    """
    serializer_class = CargoSerializer

    def get(self, request, format=None):
        cargo = Cargo()
        cargo.save()
        
        serializer = CargoSerializer(cargo)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class DeleteCargo(APIView):
    """ Delete Cargo with id """

    def delete(self,request,id):
        cargo=Cargo.objects.get(pk=id)
        cargo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)