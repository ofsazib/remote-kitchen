from django.db import models

from common.models import NameSlugDescriptionBaseModel, BaseModel


class Restaurant(NameSlugDescriptionBaseModel):
    owner = models.ForeignKey(
        'core.User', on_delete=models.CASCADE
    )
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Menu(NameSlugDescriptionBaseModel):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'core.User', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class MenuItem(NameSlugDescriptionBaseModel):
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(
        'core.User', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Order(BaseModel):
    user = models.ForeignKey(
        'core.User', on_delete=models.CASCADE
    )
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"User: {self.user}, Total Price: {self.total_price}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.order_id
