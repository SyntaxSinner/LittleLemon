from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.MenuItemList.as_view(), name='menu-item-list'),
    path('menu-items/<int:pk>/', views.MenuItemDetail.as_view(), name='menu-item-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('groups/manager/users/', views.list_managers, name='list-managers')
]