from django_filters import FilterSet
from .models import Vehicle


class VehicleFilter(FilterSet):
    class Meta:
        model = Vehicle
        fields = {
            'vehicle_serial_number': ['icontains'],
        }
