from django.db import models


# Create your models here.


class Vehicle(models.Model):
    vehicle_serial_number = models.CharField(max_length=255)
    vehicle_model = models.ForeignKey('DirectoryVehicleModel', on_delete=models.CASCADE)
    # vehicle_engine_model = models.CharField(max_length = 255)
    # vehicle_engine_serial_number = models.CharField(max_length = 255)
    # vehicle_transmission_model = models.CharField(max_length = 255)
    # vehicle_transmission_serial_number = models.CharField(max_length = 255)
    # vehicle_live_axle_model = models.CharField(max_length = 255)
    # vehicle_live_axle_serial_number = models.CharField(max_length = 255)
    # vehicle_dead_axle_model = models.CharField(max_length = 255)
    # vehicle_dead_axle_serial_number = models.CharField(max_length = 255)
    # vehicle_invoice = models.CharField(max_length = 255)
    # vehicle_shipping_date = models.CharField(max_length = 255)
    # vehicle_end_user = models.CharField(max_length = 255)
    # vehicle_shipping_address = models.CharField(max_length = 255)
    # vehicle_options = models.CharField(max_length = 255)
    # vehicle_client = models.CharField(max_length = 255)
    # vehicle_service_provider = models.CharField(max_length = 255)
    # pass


class DirectoryVehicleModel(models.Model):
    directory_vehicle_model = models.CharField(max_length=255)
    directory_vehicle_model_title = models.CharField(max_length = 255)
    directory_vehicle_model_description = models.TextField()


class Service(models.Model):  # наследуемся от класса Model
    # service_type = models.CharField(max_length = 255)
    # service_date = models.CharField(max_length = 255)
    # service_engine_hours = models.CharField(max_length = 255)
    # service_order_number = models.CharField(max_length = 255)
    # service_order_date = models.CharField(max_length = 255)
    # service_organization = models.CharField(max_length = 255)
    # service_vehicle = models.CharField(max_length = 255)
    # service_provider = models.CharField(max_length = 255)

    pass


class Reclamation(models.Model):  # наследуемся от класса Model
    # reclamation_date= models.CharField(max_length = 255)
    # reclamation_engine_hours= models.CharField(max_length = 255)
    # reclamation_malfunction= models.CharField(max_length = 255)
    # reclamation_malfunction_description= models.CharField(max_length = 255)
    # reclamation_repair_type= models.CharField(max_length = 255)
    # reclamation_placement_parts= models.CharField(max_length = 255)
    # reclamation_repair_date= models.CharField(max_length = 255)
    # reclamation_idle_time= models.CharField(max_length = 255)
    # reclamation_vehicle= models.CharField(max_length = 255)
    # reclamation_service_provider= models.CharField(max_length = 255)

    pass
