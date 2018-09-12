from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.shipment import Shipment
from ..models.factura import Factura
from ..serializers.shipment import ShipmentSerializer
from ..serializers.factura import FacturaSerializer


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


class FacturaView(APIView):
    """ Create and return new Factura for Shipment id=0 or get Factura by id """

    serializer_class = FacturaSerializer

    def get(self,request,id,factura_id):
        
        if factura_id==0:
            f=Factura()
            f.save()
        else:
            f=Factura.objects.get(pk=factura_id)

        sh = Shipment.objects.get(pk=id)
        
        sh.facturas.add(f)
        sh.save()

        factura_srlz = FacturaSerializer(f)
        return Response(factura_srlz.data,status=status.HTTP_200_OK)

class FacturasListView(APIView):
    """ Get Shipment's Facturas """
    def get(self,request,id):

        sh=Shipment.objects.get(pk=id)
        facturas = sh.facturas

        factura_serializer = FacturaSerializer(facturas,many=True)
        return Response(factura_serializer.data,status=status.HTTP_200_OK)
