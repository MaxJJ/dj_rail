from ..models import Order, InboundDoc
from ..models.place import Place
from ..models.cargo import Cargo
from ..models.shipment import Shipment
from ..models.person import Person
from ..models import Container
from ..models.factura import Factura
from ..models.invoice import Invoice
from ..models import Railbill
from ..serializers import OrderSerializer, ShipmentSerializer, InboundDocSerializer
from ..serializers.cargo import CargoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class NewOrder(APIView):

    def get(self, request):
        ord = Order()
        ord.save()

        serializer = OrderSerializer(ord)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    serializer_class = OrderSerializer

    def get(self, request, format=None):
        orders = Order.objects.all()

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        id = request.data['id']
        ord = Order.objects.get(pk=id)
        ord = self.__updatePersons(request.data, ord)
        ord = self.__updateStations(request.data, ord)
        ord = self.__updateIndocs(request.data, ord)

        serializer = OrderSerializer(ord, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def __updatePersons(self, data, order):
        consignee_id = data['consignee']['id']
        consignor_id = data['consignor']['id']
        consignee = Person.objects.get(pk=consignee_id)
        consignor = Person.objects.get(pk=consignor_id)
        order.consignee = consignee
        order.consignor = consignor
        return order

    def __updateStations(self, data, order):
        dispatch_id = data['dispatch_place']['id']
        destination_id = data['destination_place']['id']
        dispatch = Place.objects.get(pk=dispatch_id)
        destination = Place.objects.get(pk=destination_id)
        order.dispatch_place = dispatch
        order.destination_place = destination
        return order

    def __updateIndocs(self, data, order):
        docs = data['inbound_docs']
        docs_serializer = InboundDocSerializer(data=docs, many=True)
        if docs_serializer.is_valid():
            docs_serializer.save()
            for d in docs:
                docum = InboundDoc.objects.get(pk=d['id'])
                docum.__dict__.update(d)
                docum.save()
                order.inbound_docs.add(docum)
        return order


class OrdersInWork(APIView):
    """
    List all orders not closed
    """
    serializer_class = OrderSerializer

    def get(self, request, format=None):
        orders = Order.objects.all().exclude(is_closed=True)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class DeleteOrder(APIView):
    def delete(self, request, id):

        ord = Order.objects.get(pk=id)
        shipments = Shipment.objects.all().filter(order=ord)
        for sh in shipments:
            sh.delete()
        ord.delete()
        return Response('order ' + str(id) + ' is deleted', status=status.HTTP_204_NO_CONTENT)


class OneOrder(APIView):
    """
    List all snippets, or create a new snippet.
    """
    serializer_class = OrderSerializer

    def get(self, request, id, format=None):
        order = Order.objects.get(pk=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def post(self, request, id, format=None):
        order = Order.objects.get(pk=id)

        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderShipments(APIView):
    """
    List of order's shipments
    """
    serializer_class = ShipmentSerializer

    def get(self, request, id, format=None):
        order = Order.objects.get(pk=id)
        shipments = Shipment.objects.all().filter(order=order)
        serializer = ShipmentSerializer(shipments, many=True)
        return Response(serializer.data)


class InboundDocsView(APIView):

    serializer_class = InboundDocSerializer

    def get(self, request, id):
        order = Order.objects.get(pk=id)
        docs = order.inbound_docs
        serializer = InboundDocSerializer(docs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddInboundDocView(APIView):

    serializer_class = InboundDocSerializer

    def get(self, request, id, doc_id):
        order = Order.objects.get(pk=id)
        docs = order.inbound_docs
        if doc_id == 0:
            doc = InboundDoc()
            doc.save()
            docs.add(doc)
            order.save()
        else:
            doc = InboundDoc.objects.get(pk=doc_id)
            docs.remove(doc)
            order.save()
            doc.delete()

        serializer = InboundDocSerializer(docs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
