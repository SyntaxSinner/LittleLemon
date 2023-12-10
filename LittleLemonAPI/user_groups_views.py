"""
Menu Item Views

These views handle operations related to menu items.

Endpoints:
-----------------------------------------------------------------------------
| Endpoint                                     | Description                | Permissions          
-----------------------------------------------------------------------------
| GET /api/menu-items/                         | Retrieve all menu items.   | Requires authentication. 
-----------------------------------------------------------------------------
| GET /api/menu-items/{menu_item_id}/          | Retrieve a specific menu   | Requires authentication. 
|                                              | item by ID.                |                          
-----------------------------------------------------------------------------
| POST /api/menu-items/                        | Create a new menu item.    | Requires 'IsManager' permission. 
-----------------------------------------------------------------------------
| PUT /api/menu-items/{menu_item_id}/          | Update an existing menu    | Requires 'IsManager' permission. 
|                                              | item by ID.                |                          
-----------------------------------------------------------------------------
| DELETE /api/menu-items/{menu_item_id}/       | Delete a menu item by ID.  | Requires 'IsManager' permission. 
-----------------------------------------------------------------------------
"""
# The views implementation details are included below this docstring.

from django.contrib.auth.models import Group, User
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from .serializers import UserSerializer
from .permissions import IsManager

@api_view(['POST'])
@permission_classes([IsManager])
def AssignUserToGroup(request, group_name):
    """
    Assign a user to a group (manager, delivery crew) a user who isn't assigned to a group is a customer
    """
    try:
        user = User.objects.get(username=request.data['username'])
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    try:
        group = Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return JsonResponse({'error': 'Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
    user.groups.add(group)
    user.save()
    return JsonResponse({'success': 'User added to group'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsManager])
def GetManagers(request):
    """
    Return all users in the manager group
    """
    try:
        group = Group.objects.get(name='manager')
    except Group.DoesNotExist:
        return JsonResponse({'error': 'Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
    users = User.objects.filter(groups=group)
    serialized_data = UserSerializer(users, many=True)
    return JsonResponse(serialized_data.data, safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsManager])
def GetDeliveryCrew(request):
    """
    Return all users in the delivery crew group
    """
    try:
        group = Group.objects.get(name='Delivery crew')
    except Group.DoesNotExist:
        return JsonResponse({'error': 'Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
    users = User.objects.filter(groups=group)
    serialized_data = UserSerializer(users, many=True)
    return JsonResponse(serialized_data.data, safe=False, status=status.HTTP_200_OK)

@permission_classes([IsManager])
@api_view(['POST'])
def RemoveUserFromManagerGroup(request, user_id):
    """
    Remove user from the manager group
    """
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    try:
        group = Group.objects.get(name='manager')
    except Group.DoesNotExist:
        return JsonResponse({'error': 'Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
    user.groups.remove(group)
    user.save()
    return JsonResponse({'success': 'User removed from group'}, status=status.HTTP_200_OK)




