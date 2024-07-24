import django_filters
from .models import *


class CarFilter(django_filters.FilterSet):
    make = django_filters.CharFilter(field_name='make', lookup_expr='icontains')
    car_model = django_filters.NumberFilter(field_name='car_model', lookup_expr='exact')
    car_rent = django_filters.NumberFilter(field_name='car_rent', lookup_expr='exact')

    class Meta:
        model = Cars
        fields = ['make', 'car_model', 'car_rent']


