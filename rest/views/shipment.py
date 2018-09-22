from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.shipment import Shipment
from ..models.container import Container
from ..models.factura import Factura
from ..models.invoice import Invoice
from ..models.railbill import Railbill
from ..serializers.shipment import ShipmentSerializer,InvoiceSerializer
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

    # def post(self,request,id):
    #     sh=Shipment.objects.get(pk=id)
    #     invoices=request.data['invoices']


class CreateShipment(APIView):
    """ Create and return new Shipment """
    serializer_class = ShipmentSerializer

    def get(self,request):
        sh=Shipment(name='ID-')
        sh.save()
        sh=self.__set_defaults(sh)
        serializer=ShipmentSerializer(sh)
        return Response(serializer.data)

    def __set_defaults(self,shipment):
        factura=Factura()
        factura.save()
        invoice=Invoice()
        invoice.save()
        railbill=Railbill()
        railbill.save()
        shipment.facturas.add(factura)
        shipment.invoices.add(invoice)
        shipment.rw_bill=railbill
        shipment.save()
        return shipment



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

class ShipmentContainer(APIView):
    """ create or delete Shipment's container """

    def get(self,request,id,qry):
        shipment=Shipment.objects.get(pk=id)
        if qry==0:
            c=Container()
            c.save()
            shipment.container=c
            shipment.cargo_is_general=False
            
        else:
            if shipment.container:
                c=Container.objects.get(pk=shipment.container.id)
                c.delete()
                shipment.container=None
                shipment.cargo_is_general=True
        
        shipment.save()

        srlz=ShipmentSerializer(shipment)
        return Response(srlz.data,status=status.HTTP_200_OK)


class ShipmentInvoice(APIView):
    """"Create Invoice 
            return Invoice created"""

    def get(self,request,id):

        shipment = Shipment.objects.get(pk=id)
        invoice=Invoice()
        invoice.save()
        serializer=InvoiceSerializer(invoice)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
                  

    