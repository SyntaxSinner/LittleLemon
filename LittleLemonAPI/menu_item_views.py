"""
Menu Item Views

These views handle operations related to menu items.

Endpoints:
----------------------------------------------------------------------------------
| Endpoint                                     | Role       | Purpose            |
----------------------------------------------------------------------------------
| GET /api/menu-items/                         | Customer   | Retrieve all menu  |
|                                              |            | items.             |
----------------------------------------------------------------------------------
| GET /api/menu-items/{menu_item_id}/          | Customer   | Retrieve a specific|
|                                              |            | menu item by ID.   |
----------------------------------------------------------------------------------
| POST /api/menu-items/                        | Manager    | Create a new menu  |
|                                              |            | item.              |
----------------------------------------------------------------------------------
| PUT /api/menu-items/{menu_item_id}/          | Manager    | Update an existing |
|                                              |            | menu item by ID.   |
----------------------------------------------------------------------------------
| DELETE /api/menu-items/{menu_item_id}/       | Manager    | Delete a menu item |
|                                              |            | by ID.             |
----------------------------------------------------------------------------------

Note:
- Role: Specifies the role required to access the endpoint.
- Purpose: Describes the purpose of the endpoint.
"""

# The views implementation details are included below this docstring.

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.http import JsonResponse

from .models import MenuItem
from .serializers import MenuItemSerializer
from .permissions import IsManager

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetMenuItems(request):
    """
    Return all menu items
    """
    menu_items = MenuItem.objects.all()
    serialized_data = MenuItemSerializer(menu_items, many=True)
    return JsonResponse(serialized_data.data, safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetMenuItem(request, menu_item_id):
    """
    Return a menu item
    """
    try:
        menu_item = MenuItem.objects.get(pk=menu_item_id)
    except MenuItem.DoesNotExist:
        return JsonResponse({'error': 'Menu item does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serialized_data = MenuItemSerializer(menu_item)
    return JsonResponse(serialized_data.data, safe=False, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsManager])
def AddMenuItem(request):
    """
    Add a menu item
    """
    serialized_data = MenuItemSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse(serialized_data.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsManager])
def UpdateMenuItem(request, menu_item_id):
    """
    Update a menu item
    """
    try:
        menu_item = MenuItem.objects.get(pk=menu_item_id)
    except MenuItem.DoesNotExist:
        return JsonResponse({'error': 'Menu item does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serialized_data = MenuItemSerializer(menu_item, data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse(serialized_data.data, status=status.HTTP_200_OK)
    return JsonResponse(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsManager])
def DeleteMenuItem(request, menu_item_id):
    """
    Delete a menu item
    """
    try:
        menu_item = MenuItem.objects.get(pk=menu_item_id)
    except MenuItem.DoesNotExist:
        return JsonResponse({'error': 'Menu item does not exist'}, status=status.HTTP_404_NOT_FOUND)
    menu_item.delete()
    return JsonResponse({'success': 'Menu item deleted'}, status=status.HTTP_200_OK)



