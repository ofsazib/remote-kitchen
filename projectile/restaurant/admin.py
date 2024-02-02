from django.contrib import admin

from common.admin import BaseModelAdmin

from restaurant.models import (
    Restaurant,
    Menu,
    MenuItem,
    Order,
    OrderItem,
)


admin.site.register(Restaurant)
class RestaurantAdmin(BaseModelAdmin):
    pass


admin.site.register(Menu)
class MenuAdmin(BaseModelAdmin):
    pass


admin.site.register(MenuItem)
class MenuItemAdmin(BaseModelAdmin):
    pass


admin.site.register(Order)
class OrderAdmin(BaseModelAdmin):
    pass


admin.site.register(OrderItem)
class OrderItemAdmin(BaseModelAdmin):
    pass
