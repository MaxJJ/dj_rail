from ..models.invoice import Invoice
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

    
    
