from django.db import models


# Create your models here.


class Vehicle(models.Model):
    vehicle_serial_number = models.CharField(max_length=255)
    vehicle_model = models.ForeignKey('DirectoryVehicleModel', on_delete=models.CASCADE)
    vehicle_engine_model = models.ForeignKey('DirectoryVehicleEngineModel', on_delete=models.CASCADE)
    vehicle_engine_serial_number = models.CharField(max_length = 255)
    vehicle_transmission_model = models.ForeignKey('DirectoryVehicleTransmissionModel', on_delete=models.CASCADE)
    vehicle_transmission_serial_number = models.CharField(max_length = 255)
    vehicle_live_axle_model = models.ForeignKey('DirectoryVehicleLiveAxleModel', on_delete=models.CASCADE)
    vehicle_live_axle_serial_number = models.CharField(max_length = 255)
    vehicle_dead_axle_model = models.ForeignKey('DirectoryVehicleDeadAxleModel', on_delete=models.CASCADE)
    vehicle_dead_axle_serial_number = models.CharField(max_length = 255)
    vehicle_invoice = models.CharField(max_length = 255)
    vehicle_shipping_date = models.DateTimeField()
    vehicle_end_user = models.CharField(max_length = 255)
    vehicle_shipping_address = models.CharField(max_length = 255)
    vehicle_options = models.CharField(max_length = 255)
    vehicle_client = models.ForeignKey('DirectoryClientsModel', on_delete=models.CASCADE)
    vehicle_service_provider = models.ForeignKey('DirectoryServiceProvider', on_delete=models.CASCADE)


class DirectoryClientsModel(models.Model):
    directory_clients_model = models.CharField(max_length=255)
    directory_clients_model_description = models.TextField()


class DirectoryVehicleModel(models.Model):
    directory_vehicle_model = models.CharField(max_length=255)
    directory_vehicle_model_description = models.TextField()


class DirectoryVehicleEngineModel(models.Model):
    directory_vehicle_engine_model = models.CharField(max_length=255)
    directory_vehicle_engine_model_description = models.TextField()


class DirectoryVehicleTransmissionModel(models.Model):
    directory_vehicle_transmission_model = models.CharField(max_length=255)
    directory_vehicle_transmission_model_description = models.TextField()

    
class DirectoryVehicleLiveAxleModel(models.Model):
    directory_vehicle_live_axle_model = models.CharField(max_length=255)
    directory_vehicle_live_axle_model_description = models.TextField()


class DirectoryVehicleDeadAxleModel(models.Model):
    directory_vehicle_dead_axle_model = models.CharField(max_length=255)
    directory_vehicle_dead_axle_model_description = models.TextField()


class DirectoryServiceProvider(models.Model):
    directory_service_provider = models.CharField(max_length=255)
    directory_service_provider_description = models.TextField()


class Service(models.Model):
    service_type = models.ForeignKey('DirectoryServiceType', on_delete=models.CASCADE)
    service_date = models.DateTimeField()
    service_engine_hours = models.IntegerField()
    service_order_number = models.CharField(max_length = 255)
    service_order_date = models.DateTimeField()
    service_provider = models.ForeignKey('DirectoryServiceProvider', on_delete=models.CASCADE)
    service_vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)


class DirectoryServiceType(models.Model):
    directory_service_provider = models.CharField(max_length=255)
    directory_service_provider_description = models.TextField()
    

class Reclamation(models.Model):  # наследуемся от класса Model
    reclamation_date = models.DateTimeField()
    reclamation_engine_hours = models.CharField(max_length=255)
    reclamation_malfunction = models.ForeignKey('DirectoryMalfunctionType', on_delete=models.CASCADE)
    reclamation_malfunction_description = models.CharField(max_length=255)
    reclamation_repair_type = models.ForeignKey('DirectoryRepairType', on_delete=models.CASCADE)
    reclamation_replacement_parts = models.CharField(max_length=255)
    reclamation_repair_date = models.DateTimeField()
    # reclamation_idle_time = models.CharField(max_length = 255)
    reclamation_vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    reclamation_service_provider = models.ForeignKey('DirectoryServiceProvider', on_delete=models.CASCADE)


class DirectoryMalfunctionType(models.Model):
    directory_malfunction_type = models.CharField(max_length=255)
    directory_malfunction_type_description = models.TextField()


class DirectoryRepairType(models.Model):
    directory_repair_type = models.CharField(max_length=255)
    directory_repair_type_description = models.TextField()
