from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.cargo import CargoSerializer
from ..models.cargo import Cargo
from ..models.package import Package
from ..models.measure_unit import Unit
from ..models.shipment import Shipment
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

    def get(self, request,id, format=None):
        if id>0:
            cargo=Cargo.objects.get(pk=id)
        else:
            cargo = Cargo()
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