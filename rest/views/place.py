from ..models.place import Place
from ..serializers.place import PlaceSerializer

from django.http import Http404
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Places(APIView):
    """
    List all Places, or create a new Place and return one.
    """
    serializer_class = PlaceSerializer
    
    def get(self, request, format=None):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pl=None
        if request.data['id']>0:
             pl=Place.objects.get(pk=request.data['id'])
        
        if pl:
            serializer = PlaceSerializer(pl,data=request.data)
        else:
            place = Place()
            serializer = PlaceSerializer(place,data=request.data)
                
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchPlaces(APIView):
    """ Filter places by search string """
    serializer_class = PlaceSerializer

    def get(self,request,format=None):
        qst = request.query_params.get('qry')
        qst_cap = qst.capitalize()
       

        by_name = Q(place_name__icontains = request.query_params.get('qry'))
        by_cap_name = Q(place_name__icontains = qst_cap)
        by_code = Q(place_code__icontains = request.query_params.get('qry'))
        filtered_places = Place.objects.filter(by_code | by_name | by_cap_name)
       
        serializer=PlaceSerializer(filtered_places,many=True)
        return Response(serializer.data)



