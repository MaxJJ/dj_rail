from django.shortcuts import render

# Create your views here.
from .models import Order,Shipment
from .serializers import OrderSerializer,ShipmentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersInWork(APIView):
    """
    List all orders not closed
    """
    serializer_class = OrderSerializer

    def get(self,request,format=None):
        orders=Order.objects.all().exclude(is_closed=True)
        serializer=OrderSerializer(orders,many=True)
        return Response(serializer.data)



class OneOrder(APIView):
    """
    List all snippets, or create a new snippet.
    """
    serializer_class = OrderSerializer
    
    def get(self, request,id, format=None):
        order = Order.objects.get(pk=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def post(self, request,id,format=None):
        order = Order.objects.get(pk=id)
        serializer = OrderSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderShipments(APIView):
    """
    List of order's shipments
    """
    serializer_class = ShipmentSerializer

    def get(self,request,id,format=None):
        order = Order.objects.get(pk=id)
        shipments = order.shipments
        serializer = ShipmentSerializer(shipments,many=True)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        order = Order.objects.get(pk=id)
        
        serializer = ShipmentSerializer(data=request.data)
        if serializer.is_valid():
            
            shipment=serializer.save()
            order.shipments.add(serializer.instance)
            # order.save()
            shipments=order.shipments
            srlz=ShipmentSerializer(shipments,many=True)

            return Response(srlz.data,status=status.HTTP_201_CREATED)
        return Response(srlz.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderShipment(APIView):
    """
    Shipment belonging to order
    """
    serializer_class = ShipmentSerializer

    def check(self,order,pk):
        shpms=[s for s in order.shipments.all() if s.id==pk]
        if shpms:
           return True
        else:
            return False       
    
    def get(self, request,id,shipment_id, format=None):
        order = Order.objects.get(pk=id)
        if self.check(order,shipment_id):
            shipment=order.shipments.get(pk=shipment_id)
                   
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data)

    def post(self, request,id,shipment_id, format=None):
        order = Order.objects.get(pk=id)
        if self.check(order,shipment_id):
            shipment=order.shipments.get(pk=shipment_id)
            
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ShipmentSerializer(shipment,data=request.data)

        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShipmentList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    serializer_class = ShipmentSerializer
    
    def get(self, request, format=None):
        shipment = Shipment.objects.all()
        serializer = ShipmentSerializer(shipment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


