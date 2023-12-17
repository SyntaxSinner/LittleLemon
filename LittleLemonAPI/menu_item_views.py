from rest_framework.views import APIView
from rest_framework.response import Response   
from rest_framework import status

from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemsHandler(APIView):

    def get(self, request, pk=None):

        if pk is None:
            menu_item = MenuItem.objects.all()
            serializer = MenuItemSerializer(menu_item, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        try:
            instance = MenuItem.objects.get(pk=pk)
            serializer = MenuItemSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except MenuItem.DoesNotExist:
            return Response({"error" : f"menu item with pk = {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):

        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        
        instance = MenuItem.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MenuItemCategoryHandler(APIView):

    def get(self, request):

        category = request.query_params.get('category', None)
        if category is None:
            menu_item = MenuItem.objects.all()
            serializer = MenuItemSerializer(menu_item, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        try:
            instance = MenuItem.objects.filter(category=category)
            serializer = MenuItemSerializer(instance, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except MenuItem.DoesNotExist:
            return Response({"error" : f"menu item with category = {category} does not exist"}, status=status.HTTP_404_NOT_FOUND)