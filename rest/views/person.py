from ..models.person import Person
from ..serializers.person import PersonSerializer

from django.http import Http404
from ..serializers.person import PersonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q

class PersonView(APIView):
    """
    Person view 
    """
    serializer_class = PersonSerializer
    
    def get(self, request, id, format=None):
        if(id<0):
            person = Person.objects.get(pk=id)
            serializer = PersonSerializer(person)
        else:
            person = Person()
            person.save()
            serializer=PersonSerializer(person)
        return Response(serializer.data)

class AllPersonsView(APIView):

    """
    Fetch All Person items
    """

    def get(self,request):
        persons=Person.objects.all()
        serializer = PersonSerializer(persons,many=True)
        return Response(serializer.data)

        

class SavePersonView(APIView):
    """
    Save Person view 
    """
    serializer_class = PersonSerializer
    
    def post(self, request, format=None):
        id=request.data['id']
        person = Person.objects.get(pk=id)
        serializer = PersonSerializer(person,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


   
class PersonSearchView(APIView):
    """
     Search Person[] view 
    """
    serializer_class = PersonSerializer
    
    def get(self, request,format=None):
        query = request.query_params.get('query')
        query_cap=query.capitalize()

        by_name = Q(name__icontains = query)
        by_cap_name = Q(name__icontains = query_cap)
        by_code = Q(rail_code__icontains = query)
        by_street_house =Q(street_house__icontains = query) 
        by_cap_street_house =Q(street_house__icontains = query_cap)
        filtered_persons = Person.objects.filter(by_code | by_name | by_cap_name | by_street_house | by_cap_street_house)

        serializer=PersonSerializer(filtered_persons,many=True)
        return Response(serializer.data)
       


       
        