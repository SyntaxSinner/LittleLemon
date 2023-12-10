from django.urls import path
from . import menu_item_views, cart_views, order_views, user_groups_views




urlpatterns = [
    path('groups/manager/users/', user_groups_views.AssignUserToGroup),
    path('groups/manager/users/', user_groups_views.GetManagers),
    path('groups/delivery-crew/users/', user_groups_views.GetDeliveryCrew),
    path('groups/manager/users/<int:userId>/', user_groups_views.RemoveUserFromManagerGroup),
    path('menu-items/', menu_item_views.GetMenuItems),
    path('menu-items/<int:menuItemId>/', menu_item_views.GetMenuItem),
    path('menu-items/', menu_item_views.AddMenuItem),
    path('menu-items/<int:menuItemId>/', menu_item_views.UpdateMenuItem),
    path('menu-items/<int:menuItemId>/', menu_item_views.DeleteMenuItem),
]

