from ..models.order import Order,InboundDoc
from ..models.place import Place
from ..models.cargo import Cargo
from ..models.shipment import Shipment
from ..serializers.order import OrderSerializer,ShipmentSerializer,InboundDocSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class NewOrder(APIView):
    
    def get(self,request):
        ord=Order()
        ord.save()
        serializer=OrderSerializer(ord)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

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
        id=request.data['id']
        ord=Order.objects.get(pk=id)
        dispatch_id=request.data['dispatch_place']['id']
        disp=Place.objects.get(pk=dispatch_id)
        inb_cargo=self.getCargo(request.data['inbound_cargo'])
        ord.inbound_cargo.set(inb_cargo)

        shp = request.data['shipments']
        for i in shp:
            s=Shipment.objects.get(pk=i['id'])
            s.__dict__.update(i)
            s.save()
            ord.shipments.add(s)
        
        ord.dispatch_place=disp

        docs=request.data['inbound_docs']
        docs_serializer = InboundDocSerializer(data=docs,many=True)
        if docs_serializer.is_valid():
            docs_serializer.save()
            for d in docs:
                docum=InboundDoc.objects.get(pk=d['id'])
                docum.__dict__.update(d)
                docum.save()
                ord.inbound_docs.add(docum)
       
        serializer = OrderSerializer(ord,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def getCargo(self,crg):
        cargos=[]
        for c in crg:
            if 'id' in c:
                el=Cargo.objects.get(pk=c['id'])
            else:
                el=Cargo()
            for k,v in el.__dict__.items():
                if k in c:
                    setattr(el,k,c[k])
                    
            el.save()
            cargos.append(el)
            
        return cargos



    

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
        shipments = Shipment.objects.all().filter(order=order)
        serializer = ShipmentSerializer(shipments,many=True)
        return Response(serializer.data)
    

class OrderShipmentCreate(APIView):
    serializer_class = ShipmentSerializer
    def get(self,request,id):
        shipment=Shipment()
        order=Order.objects.get(pk=id)
        shipment.order=order
        shipment.save()
        serializer=ShipmentSerializer(shipment)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

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


class InboundDocsView(APIView):

    serializer_class=   InboundDocSerializer

    def get(self,request,id):
        order = Order.objects.get(pk=id)
        docs = order.inbound_docs     
        serializer=InboundDocSerializer(docs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class AddInboundDocView(APIView):

    serializer_class= InboundDocSerializer

    def get(self,request,id,doc_id):
        order = Order.objects.get(pk=id)
        docs=order.inbound_docs
        if doc_id==0:
            doc=InboundDoc()
            doc.save()
            docs.add(doc)
            order.save()
        else:
            doc = InboundDoc.objects.get(pk=doc_id)
            docs.remove(doc)
            order.save()
            doc.delete()

        serializer=InboundDocSerializer(docs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)