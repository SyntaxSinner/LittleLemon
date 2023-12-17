from django.urls import path

from LittleLemonAPI import groups_views, permission_views
from . import menu_item_views, cart_views, order_views, category_views, order_item_views




urlpatterns = [
    path('category/',category_views.CategoryHandler.as_view()),
    path('menu-items/',menu_item_views.MenuItemsHandler.as_view()),
    path('menu-items/<int:pk>/',menu_item_views.MenuItemsHandler.as_view()),
    path('menu-items/category/',menu_item_views.MenuItemCategoryHandler.as_view()),
    path('cart/',cart_views.CartHandler.as_view()),
    path('cart/<int:pk>/',cart_views.CartHandler.as_view()),
    path('order/',order_views.OrderHandler.as_view()),
    path('order/<int:pk>/',order_views.OrderHandler.as_view()),
    path('order-item/',order_item_views.OrderItemHandler.as_view()),
    path('order-item/<int:pk>/',order_item_views.OrderItemHandler.as_view()),
    path('group/',groups_views.create_group),
    path('groups/',groups_views.get_all_groups),
    path('permissions/',permission_views.list_permissions),
    path('permission/',permission_views.create_permission),
    path('permission-group/',permission_views.assign_permission_to_group),
    path('group-user/',groups_views.assign_user_to_group)
]

