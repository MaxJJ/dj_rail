from ..models.invoice import Invoice
from ..models.shipment import Shipment
from ..models.person import Person
from ..serializers.shipment import InvoiceSerializer

from django.http import Http404
from ..serializers.person import PersonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class InvoiceView(APIView):
    """
    Invoice view 
    """
    serializer_class = InvoiceSerializer
    
    def get(self, request, id, format=None):
        invoice=Invoice.objects.get(pk=id)
        serializer=InvoiceSerializer(data=invoice)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self, request, id, format=None):
        invoice=Invoice.objects.get(pk=id)
        invoice.delete()
        serializer=InvoiceSerializer(invoice)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

class CreateShipmentsInvoice(APIView):
    """ create Invoice with shipment=shipment"""
    def get(self,request,id):
        shipment=Shipment.objects.get(pk=id)
        invoice = Invoice(shipment=shipment) 
        invoice.save() 
        serializer=InvoiceSerializer(invoice)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class ShipmentsInvoices(APIView):
    """ get Invoices belonging to shipment"""

    def get(self,request,id):
        shipment=Shipment.objects.get(pk=id)
        invoices = Invoice.objects.all().filter(shipment=shipment)
         
        serializer=InvoiceSerializer(invoices,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    def post(self,request,id):
        invoices=[]
        for i in request.data:
            pk=i['id']
            invoice=Invoice.objects.get(pk=pk)
            invoice.__dict__.update(i)
            seller_id=i['seller']['id']

            buyer_id=i['buyer']['id']
            seller=Person.objects.get(pk=seller_id)
            buyer=Person.objects.get(pk=buyer_id)
            print(seller.id,buyer.id)
            invoice.seller=seller
            invoice.buyer=buyer
            invoice.save()
            invoices.append(invoice)
        serializer=InvoiceSerializer(invoices,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

