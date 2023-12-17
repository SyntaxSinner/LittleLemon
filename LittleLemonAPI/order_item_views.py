from rest_framework.views import APIView
from rest_framework.response import Response   
from rest_framework import status

from .models import OrderItem
from .serializers import OrderItemSerializer

class OrderItemHandler(APIView):

    def get(self, request, pk=None):

        if pk is None:
            menu_item = OrderItem.objects.all()
            serializer = OrderItemSerializer(menu_item, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        try:
            instance = OrderItem.objects.get(pk=pk)
            serializer = OrderItemSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except OrderItem.DoesNotExist:
            return Response({"error" : f"Order with pk = {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):

        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        
        instance = OrderItem.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)