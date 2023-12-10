from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    """
    Allows access only to authenticated users.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='manager').exists()
    
class IsDeliveryCrew(BasePermission):
    """
    Allows access only to authenticated users.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['manager', 'delivery crew']).exists()