from django.forms import ModelForm

from .models import Vehicle


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ('vehicle_serial_number', 'vehicle_model', 'vehicle_engine_model', 'vehicle_engine_serial_number',
                  'vehicle_transmission_model', 'vehicle_transmission_serial_number', 'vehicle_live_axle_model',
                  'vehicle_live_axle_serial_number', 'vehicle_dead_axle_model', 'vehicle_dead_axle_serial_number',
                  'vehicle_invoice', 'vehicle_shipping_date', 'vehicle_end_user', 'vehicle_shipping_address',
                  'vehicle_options', 'vehicle_client', 'vehicle_service_provider')
