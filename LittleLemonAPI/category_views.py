from rest_framework.views import APIView
from rest_framework.response import Response   
from rest_framework import status

from .models import Category
from .serializers import CategorySerializer

class CategoryHandler(APIView):

    def get(self, request):

        menu_item = Category.objects.all()
        serializer = CategorySerializer(menu_item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    def post(self, request):

        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        
        instance = Category.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)