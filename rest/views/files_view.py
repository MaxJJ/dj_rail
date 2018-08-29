from django.http import Http404
from django.db.models.fields.files import FileField
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from ..serializers.rtme_file_serializer import RtmeFileSerializer
from ..models.rtme_file_model import RtmeFileModel
from ..rtme_utils.gdr_service import GdrService
from rest_rail.settings import BASE_DIR
class GdrFilesView(APIView):
    """ 
    """
    serializer_class = RtmeFileSerializer
    parser_classes = (MultiPartParser, )
   
    def get(self, request):
        gdr= GdrService()
        m=RtmeFileModel()
        m.content = FileField()
        
        files = RtmeFileModel.objects.all()        
        serializer = RtmeFileSerializer(files,many=True)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      
    def post(self, request, *args, **kwargs):
    
     file_serializer = RtmeFileSerializer(data=request.data)
     
     
     if file_serializer.is_valid():
               
        file_serializer.save()
        return Response(file_serializer.data, status=status.HTTP_201_CREATED)
     else:
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)