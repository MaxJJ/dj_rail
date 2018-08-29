from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.shipment import Shipment
from ..serializers.shipment import ShipmentSerializer


class ShipmentView(APIView):
    """ get Shipment by id """
    
    serializer_class = ShipmentSerializer

    def get(self,request,id,format=None):
        sh=Shipment.objects.get(pk=id)

        if(sh):
            serializer = ShipmentSerializer(sh)
            return Response(serializer.data)
        else:
            return Response(data="NOT FOUND",status=status.HTTP_404_NOT_FOUND)

class CreateShipment(APIView):
    """ Create and return new Shipment """
    serializer_class = ShipmentSerializer

    def get(self,request):
        sh=Shipment(name='New')
        sh.save()
        serializer=ShipmentSerializer(sh)
        
        return Response(serializer.data)