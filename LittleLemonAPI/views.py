from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from django.contrib.auth.models import Group
from yaml import serialize

from .models import MenuItem, User
from .serializers import MenuItemSerializer, UserSerializer



#listing and creating multiple menu-items
class MenuItemList(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
#listing, creating, updating, and deleting a single menu-item
class MenuItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET','Post']) 
def list_managers(request):
    #list managers
    if request.method == 'GET':
        #retrieve all the managers 
        group = Group.objects.get(name='Manager')
        users = User.objects.filter(groups__name=group.name)
        serialized_data = UserSerializer(users, many=True).data

        return Response(serialized_data)
    #assign a user to managers
    if request.method == 'POST':
        username = request.data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'message' : 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        
        group = Group.objects.get(name='Manager')
        user.groups.add(group)

        return Response({'message' : 'assigned to managers'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def remove_from_managers(request, username):

    username = request.data.get('username')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'message' : 'user not found'}, status=status.HTTP_404_NOT_FOUND)
    
    group = Group.objects.get(name='Manager')
    user.groups.remove(group)

    return Response({'message' : 'removed from managers'}, status=status.HTTP_200_OK)

@api_view(['GET']) 
def list_delivery_crew(request):
    #retrieve all the managers 
    group = Group.objects.get(name='Delivery Crew')
    users = User.objects.filter(groups__name=group.name)
    serialized_data = UserSerializer(users, many=True).data

    return Response(serialized_data)

@api_view(['POST'])
def assign_to_delivery_crew(request):

    username = request.data.get('username')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'message' : 'user not found'}, status=status.HTTP_404_NOT_FOUND)
    
    group = Group.objects.get(name='Delivery Crew')
    user.groups.add(group)

    return Response({'message' : 'assigned to delivery crew'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def remove_from_delivery_crew(request):

    username = request.data.get('username')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'message' : 'user not found'}, status=status.HTTP_404_NOT_FOUND)
    
    group = Group.objects.get(name='Manager')
    user.groups.remove(group)

    return Response({'message' : 'removed from delivery crew'}, status=status.HTTP_200_OK)

