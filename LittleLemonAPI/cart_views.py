from rest_framework.views import APIView
from rest_framework.response import Response   
from rest_framework import status

from .models import Cart
from .serializers import CartSerializer

class CartHandler(APIView):

    def get(self, request, pk=None):

        if pk is None:
            menu_item = Cart.objects.all()
            serializer = CartSerializer(menu_item, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        try:
            instance = Cart.objects.get(pk=pk)
            serializer = CartSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Cart.DoesNotExist:
            return Response({"error" : f"Cart with pk = {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):

        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        
        instance = Cart.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)