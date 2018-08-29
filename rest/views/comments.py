from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.comments import CommentSerializer
from ..models.comments import Comment
from ..models.order import Order


class CommentView(APIView):
    """ Comment View
    """
    serializer_class = CommentSerializer

    def get(self, request,order_id,id, format=None):
        order=Order.objects.get(pk=order_id)
        if id>0 :
            comment=Comment.objects.get(pk=id)
        else:
            comment=Comment()
            comment.order=order
            comment.save()
        
        serializer = CommentSerializer(comment)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def post(self,request,order_id,id,format=None):
        
        comment=Comment.objects.get(pk=id)
        serializer=CommentSerializer(comment,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,order_id,id,format=None):
        comment=Comment.objects.get(pk=id)
        comment.delete()
        return Response(status=status.HTTP_200_OK)

class CommentsToOrderListView(APIView):
    def get(self,request,order_id,format=None):
        comments=Comment.objects.all().filter(order=order_id)
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
