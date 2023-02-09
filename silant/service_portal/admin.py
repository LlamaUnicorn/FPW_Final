from django.contrib import admin

from .models import Vehicle, DirectoryClientsModel, DirectoryVehicleModel, DirectoryVehicleEngineModel
from .models import DirectoryVehicleTransmissionModel, DirectoryVehicleLiveAxleModel, DirectoryVehicleDeadAxleModel, \
    DirectoryServiceProvider, Service, DirectoryServiceType, Reclamation, DirectoryMalfunctionType, DirectoryRepairType


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_serial_number', 'vehicle_serial_number', 'vehicle_shipping_date')
    list_display_links = ('vehicle_serial_number', 'vehicle_serial_number')
    search_fields = ('vehicle_serial_number', 'vehicle_serial_number')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'service_date', 'service_vehicle')
    list_display_links = ('service_type', 'service_date', 'service_vehicle')
    search_fields = ('service_type', 'service_date', 'service_vehicle')


class ReclamationAdmin(admin.ModelAdmin):
    list_display = ('reclamation_date', 'reclamation_malfunction', 'reclamation_vehicle')
    list_display_links = ('reclamation_date', 'reclamation_malfunction', 'reclamation_vehicle')
    search_fields = ('reclamation_date', 'reclamation_malfunction', 'reclamation_vehicle')


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Reclamation, ReclamationAdmin)
admin.site.register(DirectoryClientsModel)
admin.site.register(DirectoryVehicleModel)
admin.site.register(DirectoryVehicleEngineModel)
admin.site.register(DirectoryVehicleTransmissionModel)
admin.site.register(DirectoryVehicleLiveAxleModel)
admin.site.register(DirectoryVehicleDeadAxleModel)
admin.site.register(DirectoryServiceProvider)
admin.site.register(DirectoryServiceType)
admin.site.register(DirectoryMalfunctionType)
admin.site.register(DirectoryRepairType)
