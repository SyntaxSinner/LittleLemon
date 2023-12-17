from os import name
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.csrf import csrf_exempt as csrf
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response   


@api_view(['GET'])
def list_permissions(request):
    permissions = Permission.objects.all()
    permission_list = [
        {
            'name': permission.name,
            'content_type': permission.content_type.model,
            'codename': permission.codename
        }
        for permission in permissions
    ]
    return Response({'permissions': permission_list})

@api_view(['POST'])
def create_permission(request):
    permission_name = request.data.get('name')
    model_name = request.data.get('model_name')  
    codename = request.data.get('codename') 

    try:
        model = ContentType.objects.get(model=model_name.lower()).model_class()
        content_type = ContentType.objects.get_for_model(model)
        
        if permission_name and content_type and codename:
            permission, created = Permission.objects.get_or_create(
                name=permission_name,
                content_type=content_type,
                codename=codename
            )
            if created:
                return Response({'message': f'Permission {permission_name} created successfully'})
            else:
                return Response({'message': f'Permission {permission_name} already exists'})
        else:
            return Response({'message': 'Incomplete data provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    except ContentType.DoesNotExist:
        return Response({'message': 'Invalid model name provided'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def assign_permission_to_group(request):
    group_name = request.data.get('group_name')
    permission_codename = request.data.get('permission_codename')

    if group_name and permission_codename:
        group = Group.objects.get(name=group_name)
        permission = Permission.objects.get(codename=permission_codename)
        group.permissions.add(permission)
        return Response({'message': f'Permission {permission_codename} assigned to group {group_name}'})
    else:
        return Response({'message': 'Incomplete data provided'}, status=status.HTTP_400_BAD_REQUEST)