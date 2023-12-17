from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self) -> str:
        return self.title
    class Meta:
        permissions = [
            ('can_view_category', 'Can view category'),
            ('can_edit_category', 'Can edit category'),
            ('can_delete_category', 'Can delete category'),
            ('can_add_category', 'Can add category'),
        ]

class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title
    class Meta:
        permissions = [
            ('can_view_menu_item', 'Can view menu item'),
            ('can_edit_menu_item', 'Can edit menu item'),
            ('can_delete_menu_item', 'Can delete menu item'),
            ('can_add_menu_item', 'Can add menu item'),
        ]

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.user.username} - {self.menu_item.title}'

    class Meta:
        unique_together = ('user', 'menu_item') #each cart needs to have a unique user and menu item
        permissions = [
            ('can_view_cart', 'Can view cart'),
            ('can_edit_cart', 'Can edit cart'),
            ('can_delete_cart', 'Can delete cart'),
            ('can_add_cart', 'Can add cart'),
        ]

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivery_crew', null=True)
    status = models.BooleanField(db_index=True, default=False)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)

    def __str__(self) -> str:
        return f'{self.user.username} - {self.date}'
    class Meta:
        permissions = [
            ('can_view_order', 'Can view order'),
            ('can_edit_order', 'Can edit order'),
            ('can_delete_order', 'Can delete order'),
            ('can_add_order', 'Can add order'),
        ]
class OrderItem(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menu_item')
        permissions = [
            ('can_view_order_item', 'Can view order item'),
            ('can_edit_order_item', 'Can edit order item'),
            ('can_delete_order_item', 'Can delete order item'),
            ('can_add_order_item', 'Can add order item'),
        ]

    def __str__(self) -> str:
        return f'{self.order.username} - {self.menu_item.title}'


