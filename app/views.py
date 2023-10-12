from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Bts
from .serializers import BtsSerializers

# Create your views here.
class BtsMember(APIView):
    def get(self,request):
        obj = Bts.objects.all()
        serializer = BtsSerializers(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = BtsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class BtsInfo(APIView):
    def get(self, request, id):
        try:
            obj = Bts.objects.get(id=id)
        except Bts.doesNotExist:
            msg = {"msg":"not found "}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = BtsSerializer(obj)
        return Respose(serializer.data,status=status.HTTP_200_OK)
     
    def delete(self,request,id):
        try:
            obj = Bts.objects.get(id=id)

        except Bts.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"deleted"}, status=status.HTTP_204_NO_CONTENT)
    
        