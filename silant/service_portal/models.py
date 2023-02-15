from django.db import models

# Create your models here.


class Vehicle(models.Model):
    vehicle_serial_number = models.CharField(max_length=255)
    vehicle_model = models.ForeignKey('DirectoryVehicleModel', on_delete=models.CASCADE)
    vehicle_engine_model = models.ForeignKey('DirectoryVehicleEngineModel', on_delete=models.CASCADE)
    vehicle_engine_serial_number = models.CharField(max_length=255)
    vehicle_transmission_model = models.ForeignKey('DirectoryVehicleTransmissionModel', on_delete=models.CASCADE)
    vehicle_transmission_serial_number = models.CharField(max_length=255)
    vehicle_live_axle_model = models.ForeignKey('DirectoryVehicleLiveAxleModel', on_delete=models.CASCADE)
    vehicle_live_axle_serial_number = models.CharField(max_length=255)
    vehicle_dead_axle_model = models.ForeignKey('DirectoryVehicleDeadAxleModel', on_delete=models.CASCADE)
    vehicle_dead_axle_serial_number = models.CharField(max_length=255)
    vehicle_invoice = models.CharField(null=True, blank=True, max_length=255)
    vehicle_shipping_date = models.DateField()
    vehicle_end_user = models.CharField(max_length=255)
    vehicle_shipping_address = models.CharField(max_length=255)
    vehicle_options = models.CharField(max_length=255)
    vehicle_client = models.ForeignKey('DirectoryClientsModel', on_delete=models.CASCADE)
    vehicle_service_provider = models.ForeignKey('DirectoryServiceProvider', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Vehicles'
        verbose_name = 'Vehicle'
        ordering = ['-vehicle_shipping_date']

    def __str__(self):
        return self.vehicle_serial_number


class DirectoryClientsModel(models.Model):
    directory_clients_model = models.CharField(max_length=255)
    directory_clients_model_description = models.TextField()

    def __str__(self):
        return self.directory_clients_model


class DirectoryVehicleModel(models.Model):
    directory_vehicle_model = models.CharField(max_length=255)
    directory_vehicle_model_description = models.TextField()

    def __str__(self):
        return self.directory_vehicle_model

    class Meta:
        verbose_name_plural = 'Vehicle Models'
        verbose_name = 'Vehicle Model'


class DirectoryVehicleEngineModel(models.Model):
    directory_vehicle_engine_model = models.CharField(max_length=255)
    directory_vehicle_engine_model_description = models.TextField()

    def __str__(self):
        return self.directory_vehicle_engine_model


class DirectoryVehicleTransmissionModel(models.Model):
    directory_vehicle_transmission_model = models.CharField(max_length=255)
    directory_vehicle_transmission_model_description = models.TextField()

    def __str__(self):
        return self.directory_vehicle_transmission_model

class DirectoryVehicleLiveAxleModel(models.Model):
    directory_vehicle_live_axle_model = models.CharField(max_length=255)
    directory_vehicle_live_axle_model_description = models.TextField()

    def __str__(self):
        return self.directory_vehicle_live_axle_model


class DirectoryVehicleDeadAxleModel(models.Model):
    directory_vehicle_dead_axle_model = models.CharField(max_length=255)
    directory_vehicle_dead_axle_model_description = models.TextField()

    def __str__(self):
        return self.directory_vehicle_dead_axle_model


class DirectoryServiceProvider(models.Model):
    directory_service_provider = models.CharField(max_length=255)
    directory_service_provider_description = models.TextField()

    def __str__(self):
        return self.directory_service_provider


class Service(models.Model):
    service_type = models.ForeignKey('DirectoryServiceType', on_delete=models.CASCADE)
    service_date = models.DateField()
    service_engine_hours = models.IntegerField()
    service_order_number = models.CharField(max_length=255)
    service_order_date = models.DateField()
    service_provider = models.ForeignKey('DirectoryServiceProvider', on_delete=models.CASCADE)
    service_vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Services'
        verbose_name = 'Service'
        ordering = ['-service_date']


class DirectoryServiceType(models.Model):
    directory_service_type = models.CharField(max_length=255)
    directory_service_type_description = models.TextField()

    def __str__(self):
        return self.directory_service_type


class Reclamation(models.Model):
    reclamation_date = models.DateField()
    reclamation_engine_hours = models.CharField(max_length=255)
    reclamation_malfunction = models.ForeignKey('DirectoryMalfunctionType', on_delete=models.CASCADE)
    reclamation_malfunction_description = models.CharField(max_length=255)
    reclamation_repair_type = models.ForeignKey('DirectoryRepairType', on_delete=models.CASCADE)
    reclamation_replacement_parts = models.CharField(max_length=255)
    reclamation_repair_date = models.DateField()
    reclamation_idle_time = models.BigIntegerField(blank=True, null=True)
    reclamation_vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    reclamation_service_provider = models.ForeignKey('DirectoryServiceProvider', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Reclamations'
        verbose_name = 'Reclamation'
        ordering = ['-reclamation_date']

    def save(self, *args, **kwargs):
        # self.reclamation_idle_time = self.reclamation_repair_date - self.reclamation_date
        self.reclamation_idle_time = (self.reclamation_repair_date - self.reclamation_date).days
        super().save(*args, **kwargs)


class DirectoryMalfunctionType(models.Model):
    directory_malfunction_type = models.CharField(max_length=255)
    directory_malfunction_type_description = models.TextField()

    def __str__(self):
        return self.directory_malfunction_type


class DirectoryRepairType(models.Model):
    directory_repair_type = models.CharField(max_length=255)
    directory_repair_type_description = models.TextField()

    def __str__(self):
        return self.directory_repair_type
