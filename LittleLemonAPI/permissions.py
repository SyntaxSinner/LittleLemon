from rest_framework.permissions import BasePermission, IsAdminUser

class IsManager(BasePermission):
    """
    Allows access only to managers and admin
    """
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.groups.filter(name='manager').exists()
    
class IsDeliveryCrew(BasePermission):
    """
    Allows access only to delivery crew admins and managers
    """
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.groups.filter(name__in=['manager', 'delivery crew']).exists()