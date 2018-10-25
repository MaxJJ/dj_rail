from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.cargo import CargoSerializer
from ..models.cargo import Cargo
from ..models.package import Package
from ..models.measure_unit import Unit
from ..models.shipment import Shipment
from ..models.factura import Factura
from django.db.models import Q

class NewCargo(APIView):
    """ Get new created Cargo.
    """
    serializer_class = CargoSerializer

    def get(self, request, format=None):
        cargo = Cargo()
        cargo.save()
        
        serializer = CargoSerializer(cargo)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class DeleteCargo(APIView):
    """ Delete Cargo with id """

    def delete(self,request,id):
        cargo=Cargo.objects.get(pk=id)
        cargo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class CargoItemView(APIView):
    """ Get  Cargo by id or create new if id=0.
    """
    serializer_class = CargoSerializer

    def get(self, request,id,cargo_id, format=None):
        if cargo_id>0:
            cargo=Cargo.objects.get(pk=cargo_id)
        else:
            cargo = Cargo()
        factura=Factura.objects.get(pk=id)
        cargo.factura=factura
        cargo.save()
        
        serializer = CargoSerializer(cargo)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    

    def delete(self,request,id):
        cargo=Cargo.objects.get(pk=id)
        cargo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self,request,id):
        cargo=Cargo.objects.get(pk=id)
        
        unit = Unit.objects.get(pk=request.data['unit']['id'])
        cargo.unit = unit
        pack = Package.objects.get(pk=request.data['package']['id'])
        cargo.package = pack


        serializer=CargoSerializer(cargo,request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class FacturasCargo(APIView):
    """ Get all cargo items for Factura with id @param id """
    def get(self,request,id):
        factura=Factura.objects.get(pk=id)
        cargo=Cargo.objects.all().filter(factura=factura)

        serializer=CargoSerializer(cargo,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,id):
        cargo=[]
        for c in request.data:
            c_id=c['id']
            item = Cargo.objects.get(pk=c_id)
            serializer=CargoSerializer(item,data=c)
            if serializer.is_valid():
                item=serializer.save()
                cargo.append(item)
        cargo_serializer=CargoSerializer(cargo,many=True)
        return Response(cargo_serializer.data,status=status.HTTP_200_OK)


class CargoByShipmentView(APIView):

    def get(self,request,id):
        sh= Shipment.objects.get(pk=id)
        # cargo_set = Cargo.objects.all().filter(shipment=sh)
        cargo_set = Cargo.objects.all()
        serializer=CargoSerializer(cargo_set,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)


class CargoSearchView(APIView):

    def get(self,request):
        query=request.query_params.get('qry')
        query_cap = query.capitalize()
        
        by_query= Q(description__icontains = query)
        by_cap_query = Q(description__icontains = query_cap)
        filtered = Cargo.objects.filter(by_query | by_cap_query )
       
        serializer=CargoSerializer(filtered,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)        

class IndexedCargoView(APIView):

    def get(self,request):
        cargo = Cargo.objects.all().filter(is_indexed=True)
        serializer=CargoSerializer(cargo,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 