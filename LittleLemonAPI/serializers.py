#third party imports
from rest_framework import serializers
#local imports
from .models import *
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('slug', 'title',  'pk')

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('title', 'price', 'featured', 'category', 'pk')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user', 'menu_item', 'quantity', 'unit_price', 'price')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'delivery_crew', 'status', 'total', 'date')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('order', 'menu_item', 'quantity', 'unit_price', 'price')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'id')
