from django_filters import FilterSet
from .models import Vehicle


class VehicleFilter(FilterSet):
    class Meta:
        model = Vehicle
        fields = {
            'vehicle_model' = ['icontains'],
            'vehicle_engine_model' = ['icontains'],
        }
