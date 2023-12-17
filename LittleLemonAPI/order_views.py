from rest_framework.views import APIView
from rest_framework.response import Response   
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Order
from .serializers import OrderSerializer

class OrderHandler(APIView):

    def get(self, request, pk=None):

        if pk is None:
            menu_item = Order.objects.all()
            serializer = OrderSerializer(menu_item, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        try:
            instance = Order.objects.get(pk=pk)
            serializer = OrderSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Order.DoesNotExist:
            return Response({"error" : f"Order with pk = {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        
        instance = Order.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AssignOrderToDeliveryCrew(APIView):

    def post(self, request):
        order_id = request.data.get('order_id')
        delivery_crew_name = request.data.get('delivery_crew_name')

        if order_id and delivery_crew_name:
            try:
                order = Order.objects.get(id=order_id)
                order.delivery_crew = delivery_crew_name
                order.save()
                return Response({'message': f'Order {order_id} assigned to delivery crew {delivery_crew_name}'})
            except Order.DoesNotExist:
                return Response({'message': 'Order does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'Incomplete data provided'}, status=status.HTTP_400_BAD_REQUEST)