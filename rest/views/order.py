from ..models.order import Order,InboundDoc
from ..models.place import Place
from ..models.cargo import Cargo
from ..models.shipment import Shipment
from ..models.person import Person
from ..models.container import Container
from ..models.factura import Factura
from ..models.invoice import Invoice
from ..models.railbill import Railbill
from ..serializers.order import OrderSerializer,ShipmentSerializer,InboundDocSerializer
from ..serializers.cargo import CargoSerializer
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
        ord=self.__updatePersons(request.data,ord)
        ord=self.__updateStations(request.data,ord)
        ord=self.__updateIndocs(request.data,ord)

       
        serializer = OrderSerializer(ord,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def __updatePersons(self,data,order):
        consignee_id=data['consignee']['id']
        consignor_id=data['consignor']['id']
        consignee=Person.objects.get(pk=consignee_id)
        consignor=Person.objects.get(pk=consignor_id)
        order.consignee=consignee
        order.consignor=consignor
        return order
    def __updateStations(self,data,order):
        dispatch_id=data['dispatch_place']['id']
        destination_id=data['destination_place']['id']
        dispatch=Place.objects.get(pk=dispatch_id)
        destination=Place.objects.get(pk=destination_id)
        order.dispatch_place=dispatch
        order.destination_place=destination
        return order
        
    def __updateIndocs(self,data,order):
        docs=data['inbound_docs']
        docs_serializer = InboundDocSerializer(data=docs,many=True)
        if docs_serializer.is_valid():
            docs_serializer.save()
            for d in docs:
                docum=InboundDoc.objects.get(pk=d['id'])
                docum.__dict__.update(d)
                docum.save()
                order.inbound_docs.add(docum)
        return order


    

class OrdersInWork(APIView):
    """
    List all orders not closed
    """
    serializer_class = OrderSerializer

    def get(self,request,format=None):
        orders=Order.objects.all().exclude(is_closed=True)
        serializer=OrderSerializer(orders,many=True)
        return Response(serializer.data)

class DeleteOrder(APIView):
    def delete(self,request,id):
        
        ord=Order.objects.get(pk=id)
        shipments=Shipment.objects.all().filter(order=ord)
        for sh in shipments:
            sh.delete()
        ord.delete()
        return Response('order '+ str(id) +' is deleted', status=status.HTTP_204_NO_CONTENT)

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
        shipment= self.__set_defaults(id)
        serializer=ShipmentSerializer(shipment)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    def __set_defaults(self,id):
        shipment=Shipment(name='ID-')
        order=Order.objects.get(pk=id)
        shipment.order=order

        

        factura=Factura()
        factura.save()
        invoice=Invoice()
        invoice.save()
        railbill=Railbill()
        railbill.save()
        shipment.save()
        shipment.facturas.set([factura,])
        shipment.invoices.set([invoice,])
        shipment.rw_bill=railbill
        shipment.save()
        return shipment

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

class OrderShipmentGetSave(APIView):
    """
    Get order's shipment - get / save order's Shipment - post
    """
    serializer_class = ShipmentSerializer

    def get(self,request,id,shipment_id):
        shipment=Shipment.objects.get(pk=id)
        serializer=ShipmentSerializer(data=shipment)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,id,shipment_id):
        order=Order.objects.get(pk=id)
        shipment=Shipment.objects.get(pk=shipment_id)
        
        req_container=request.data['container']
        req_facturas=request.data['facturas']
        shipment.facturas.set(self.__updateFacturas(req_facturas)) 
        if req_container is not None:
            container=Container.objects.get(pk=req_container['id'])
            container.__dict__.update(req_container)
            container.save()
            shipment.container=container
        else:
            shipment.cargo_is_general=True
            
        req_invoices = request.data['invoices']

        for i in req_invoices:
            inv = Invoice.objects.get(pk=i['id'])
            inv.__dict__.update(i)
            inv.save()
            shipment.invoices.add(inv)

        shipment.order=order
        shipment.save()
        serializer=ShipmentSerializer(shipment,data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def __updateFacturas(self,req):
        updated=[]
        for f in req:
            factura = Factura.objects.get(pk=f['id'])
            cargo=f['cargo']
            for c in cargo:
                cargo_item=Cargo.objects.get(pk=c['id'])
                cargo_item.__dict__.update(c)
                c_ser = CargoSerializer(cargo_item,data=c)

                if c_ser.is_valid():
                   c_ser.save()
               
                cargo_item.__dict__.update(c_ser.data)   
            
                cargo_item.save()
                factura.cargo.add(cargo_item)
            updated.append(factura)
        return updated


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