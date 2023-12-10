"""
Cart Management Endpoints

These endpoints manage operations related to a user's shopping cart.

Endpoints:
-----------------------------------------------------------------------------
| Endpoint                       | Role       | Purpose                   |
-----------------------------------------------------------------------------
| /api/cart/menu-items           | Customer   | Returns current items in  |
|                                |            | the cart for the current  |
|                                |            | user token.               |
-----------------------------------------------------------------------------
| /api/cart/menu-items           | Customer   | Adds the menu item to the |
|                                |            | cart. Sets the            |
|                                |            | authenticated user as the |
|                                |            | user id for these cart    |
|                                |            | items.                    |
-----------------------------------------------------------------------------
| /api/cart/menu-items           | Customer   | Deletes all menu items    |
|                                |            | created by the current    |
|                                |            | user token.               |
-----------------------------------------------------------------------------

Note:
- Role: Specifies the role required to access the endpoint.
- Purpose: Describes the purpose of the endpoint.
"""
# The implementation details for these endpoints would be added below this docstring.
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.http import JsonResponse

from .serializers import CartSerializer
from .models import Cart  

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetCart(request):
    """
    Return all menu items
    """
    cart_items = Cart.objects.all()
    serialized_data = CartSerializer(cart_items, many=True)
    return JsonResponse(serialized_data.data, safe=False, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AddToCart(request):
    authenticated_user = request.user
    cart_items_data = request.data.get('cart_items', [])

    valid_cart_items = []
    for cart_item_data in cart_items_data:
        cart_item_data['user'] = authenticated_user.id
        cart_item_serializer = CartSerializer(data=cart_item_data)
        if cart_item_serializer.is_valid():
            cart_item_serializer.save()
            valid_cart_items.append(cart_item_serializer.data)
        else:
            return JsonResponse(cart_item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse(valid_cart_items, safe=False, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteCart(request):
    authenticated_user = request.user
    cart_items = Cart.objects.filter(user=authenticated_user.id)
    cart_items.delete()
    return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)