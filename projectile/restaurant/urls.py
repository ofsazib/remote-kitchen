from django.urls import path
from restaurant.views import (
    RestaurantListCreate,
    RestaurantDetails,
    MenuListCreate,
    MenuDetails,
    MenuItemListCreate,
    MenuItemDetails,
    OrderListCreate,
)

urlpatterns = [
    path('', RestaurantListCreate.as_view(), name='restaurant-list-create'),
    path('<int:id>/', RestaurantDetails.as_view(), name='restaurant-details'),
    path('menus/', MenuListCreate.as_view(), name='menu-list-create'),
    path('menus/<int:id>/', MenuDetails.as_view(), name='menu-details'),
    path('menu/items/', MenuItemListCreate.as_view(), name='menu-item-list-create'),
    path('menu/items/<int:id>/', MenuItemDetails.as_view(), name='menu-item-details'),
    path('orders', OrderListCreate.as_view(), name='order-list-create'),
]
