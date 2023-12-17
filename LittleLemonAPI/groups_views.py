from django.contrib.auth.models import Group, User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_all_groups(request):
    groups = Group.objects.all()
    return Response(data={'groups': groups.values()}, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_group(request):
    group_name = request.data.get('name')  
    if group_name:
        new_group, created = Group.objects.get_or_create(name=group_name)
        if created:
            return Response({'message': f'Group {group_name} created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': f'Group {group_name} already exists'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Name field is required'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def assign_user_to_group(request):
    username = request.data.get('username')
    group_name = request.data.get('group_name')

    if username and group_name:
        try:
            user = User.objects.get(username=username)
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            return Response({'message': f'User {username} assigned to group {group_name}'})
        except User.DoesNotExist:
            return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Group.DoesNotExist:
            return Response({'message': 'Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': f'Error: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'message': 'Incomplete data provided'}, status=status.HTTP_400_BAD_REQUEST)

    