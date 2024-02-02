from django_filters import FilterSet, filters

from .models import Menu


class MenuListFilter(FilterSet):
    restaurant = filters.CharFilter(
        field_name='restaurant__id'
    )

    class Meta:
        model = Menu
        fields = []
