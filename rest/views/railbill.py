from ..models.order import Order,InboundDoc
from ..models.place import Place
from ..models.cargo import Cargo
from ..models.shipment import Shipment
from ..models.person import Person
from ..models.container import Container
from ..models.factura import Factura
from ..models.invoice import Invoice
from ..models.railbill import Railbill
from ..models.road_section import RoadSection
from ..serializers.order import OrderSerializer,ShipmentSerializer,InboundDocSerializer
from ..serializers.cargo import CargoSerializer
from ..serializers.shipment import RailBillSerializer,RoadSectionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RailbillView(APIView):
    def get(self,request,id):
        shipment=Shipment.objects.get(pk=id)
        if Railbill.objects.filter(shipment=shipment).exists():
            rwb=Railbill.objects.get(shipment=shipment)
        else:
            rwb=Railbill(shipment=shipment)
            rwb.save()
        rwb_serializer=RailBillSerializer(rwb)
        return Response(rwb_serializer.data,status=status.HTTP_200_OK)

    def post(self,request,id):
        rwb_id=request.data['id']
        rwb=Railbill.objects.get(pk=rwb_id)
        rwb_serializer=RailBillSerializer(rwb,request.data)
        if rwb_serializer.is_valid():
            rwb_serializer.save()
            return Response(rwb_serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(rwb_serializer.errors)



class CreateRailbill(APIView):

    def get(self,request,id):
        shipment=Shipment.objects.get(pk=id)
        rwb=Railbill(shipment=shipment)
        rwb.save()
        rwb_serializer=RailBillSerializer(rwb)
        return Response(rwb_serializer.data,status=status.HTTP_200_OK)

class CreateRoadSection(APIView):

    def get(self,request,id):
        section=RoadSection()
        section.save()

        serializer=RoadSectionSerializer(section)
        return Response(serializer.data,status=status.HTTP_200_OK)

        