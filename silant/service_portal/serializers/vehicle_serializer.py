from rest_framework import serializers
from service_portal.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('vehicle_serial_number', 'vehicle_engine_serial_number', 'vehicle_transmission_serial_number')


class VehicleManagersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('vehicle_serial_number', 'vehicle_engine_serial_number', 'vehicle_transmission_serial_number', 'vehicle_shipping_date', 'vehicle_options')
