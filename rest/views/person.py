from ..models.person import Person
from ..serializers.person import PersonSerializer

from django.http import Http404
from ..serializers.person import PersonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PersonView(APIView):
    """
    Person views 
    """
    serializer_class = PersonSerializer
    
    def get(self, request, id, format=None):
        person = Person.objects.get(pk=id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

   