from django.contrib import admin

from .models import Vehicle, DirectoryVehicleModel, DirectoryVehicleEngineModel, DirectoryVehicleLiveAxleModel
from .models import DirectoryVehicleDeadAxleModel, DirectoryClientsModel, DirectoryVehicleTransmissionModel, DirectoryServiceProvider

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_serial_number', 'vehicle_model', 'vehicle_shipping_date')
    list_display_links = ('vehicle_serial_number', 'vehicle_model')
    search_fields = ('vehicle_serial_number', 'vehicle_model')


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(DirectoryVehicleModel)
admin.site.register(DirectoryVehicleEngineModel)
admin.site.register(DirectoryVehicleLiveAxleModel)
admin.site.register(DirectoryVehicleDeadAxleModel)
admin.site.register(DirectoryClientsModel)
admin.site.register(DirectoryVehicleTransmissionModel)
admin.site.register(DirectoryServiceProvider)
