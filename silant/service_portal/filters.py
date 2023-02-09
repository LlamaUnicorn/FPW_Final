from django_filters import FilterSet, CharFilter
from .models import Vehicle


class VehicleFilter(FilterSet):
    vehicle_model = CharFilter(field_name='vehicle_model__directory_vehicle_model', lookup_expr='icontains')
    class Meta:
        model = Vehicle
        fields = ['vehicle_model']
