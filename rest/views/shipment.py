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


class ShipmentView(APIView):
    """ get and post Shipment by id """
    
    serializer_class = ShipmentSerializer

    def get(self,request,id,format=None):
        sh=Shipment.objects.get(pk=id)

        if(sh):
            serializer = ShipmentSerializer(sh)
            return Response(serializer.data)
        else:
            return Response(data="NOT FOUND",status=status.HTTP_404_NOT_FOUND)

    def post(self,request,id):
        sh=Shipment.objects.get(pk=id)
        is_general = request.data['cargo_is_general']
        if is_general is not True:
           container= self.__updateContainer(request.data['container'])
           sh.container=container

        else:
            pass
        serializer = ShipmentSerializer(sh,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def __updateContainer(self,container):
        id=container['id']
        print(id)
        if id==0:

            c=Container()
            c.save()
        else:
            c=Container.objects.get(pk=id)
            c.save()
        
        cont_serializer = ContainerSerializer(c,data=container)
        if cont_serializer.is_valid():
           ctr= cont_serializer.save()
           return ctr
        else:
            return None
        

class CreateShipment(APIView):
    """ Create and return new Shipment """
    serializer_class = ShipmentSerializer

    def get(self,request,id):
        order=Order.objects.get(pk=id)
        sh=Shipment(name='',order=order)
        sh.save()
        serializer=ShipmentSerializer(sh)
        return Response(serializer.data)



class OrdersShipments(APIView):
    """
    List all snippets, or create a new snippet.
    """
    serializer_class = ShipmentSerializer
    
    def get(self, request,id, format=None):
        order=Order.objects.get(pk=id)
        shipments = Shipment.objects.all().filter(order=order)
        
        serializer = ShipmentSerializer(shipments, many=True)
        return Response(serializer.data)






                  
class ShipmentInfoView(APIView):
    """ Update Shipment's info  name,description,container """

    def post(self,request,id):
        shipment = Shipment.objects.get(pk=id)
        shipment.name = request.data['name']
        shipment.description = request.data['description']
        shipment.cargo_is_general=request.data['isGeneral']

        if request.data['isGeneral']==True:
            if shipment.container is not None:
                # container=Container.objects.get(pk=shipment.container.id)
                container_id =shipment.container.id
                shipment.container=None
                container=Container.objects.get(pk=container_id)
                container.delete()
                
            else:
                pass

        else:
            print(request.data['container'])
            cont_id=request.data['container']['id']
            
            if cont_id==0:
                container=Container()
                container.save()
            else:
                container=Container.objects.get(pk=cont_id)
                container.save()

            container_serializer=ContainerSerializer(container,data=request.data['container'])
            if container_serializer.is_valid():
                container=container_serializer.save()
            else:
                print(container_serializer.errors)

            shipment.container=container
        
        shipment.save()

        shipment_serializer = ShipmentSerializer(shipment)
        return Response(shipment_serializer.data,status=status.HTTP_200_OK)
        # if shipment_serializer.is_valid():
        #     shipment_serializer.save()
        #     return Response(shipment_serializer.data,status=status.HTTP_200_OK)
        # else:
        #     return Response(shipment_serializer.errors)

                    

            

            
            


    
    