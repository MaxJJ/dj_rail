from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.order import Order
from ..models.shipment import Shipment
from ..models.container import Container
from ..models.factura import Factura
from ..models.invoice import Invoice
from ..models.railbill import Railbill
from ..serializers.shipment import ShipmentSerializer,InvoiceSerializer,ContainerSerializer
from ..serializers.factura import FacturaSerializer


class FacturaView(APIView):
    """ Factura get post by id """

    serializer_class = FacturaSerializer

    def get(self,request,id):
        
        f=Factura.objects.get(pk=id)

        factura_srlz = FacturaSerializer(f)
        return Response(factura_srlz.data,status=status.HTTP_200_OK)

    def post(self,request,id):

        f=Factura.objects.get(pk=id)
        factura_srlz = FacturaSerializer(f,data=request.data)
        if factura_srlz.is_valid():
            
            factura_srlz.save()
            return Response(factura_srlz.data,status=status.HTTP_200_OK)


class FacturasListView(APIView):
    """ Get Shipment's Facturas """
    def get(self,request,id):

        sh=Shipment.objects.get(pk=id)
        facturas = Factura.objects.all().filter(shipment=sh)

        factura_serializer = FacturaSerializer(facturas,many=True)
        return Response(factura_serializer.data,status=status.HTTP_200_OK)

class CreateFactura(APIView):
    """ Create new Factura """
    def get(self,request,id):
        sh=Shipment.objects.get(pk=id)
        factura=Factura()
        factura.shipment=sh
        factura.save()
        factura_serializer = FacturaSerializer(factura)
        return Response(factura_serializer.data,status=status.HTTP_200_OK)