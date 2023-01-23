from django.db import models

# Create your models here.


class Vehicles(models.Model):  # наследуемся от класса Model
    # vehicle_serial_number = models.CharField(max_length = 255)
    # vehicle_model = models.CharField(max_length = 255)
    # engine_model = models.CharField(max_length = 255)
    # engine_serial_number = models.CharField(max_length = 255)
    # transmission_model = models.CharField(max_length = 255)
    # transmission_serial_number = models.CharField(max_length = 255)
    # live_axle_model = models.CharField(max_length = 255)
    # live_axle_serial_number = models.CharField(max_length = 255)
    # dead_axle_model = models.CharField(max_length = 255)
    # dead_axle_serial_number = models.CharField(max_length = 255)
    # invoice = models.CharField(max_length = 255)
    # shipping_date = models.CharField(max_length = 255)
    # end_user = models.CharField(max_length = 255)
    # shipping_address = models.CharField(max_length = 255)
    # options = models.CharField(max_length = 255)
    # client = models.CharField(max_length = 255)
    # service_provider = models.CharField(max_length = 255)

    pass


class Services(models.Model):  # наследуемся от класса Model
    pass


class Reclamations(models.Model):  # наследуемся от класса Model
    pass
