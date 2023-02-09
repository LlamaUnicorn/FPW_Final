from django.urls import path

from .views import *

urlpatterns = [
    path('create/', VehicleCreateView.as_view(), name='create'),
    path('', index, name='index'),
    path('vehicle_serial_number/<int:pk>', directory_vehicle_model_view, name='directory_vehicle_model_view'),
    path('vehicle_engine_model/<int:pk>', directory_vehicle_engine_model_view, name='directory_vehicle_engine_model_view'),
    path('vehicle_transmission_model/<int:pk>', directory_vehicle_transmission_model_view, name='directory_vehicle_transmission_model_view'),
    path('vehicle_live_axle_model/<int:pk>', directory_vehicle_live_axle_model_view, name='directory_vehicle_live_axle_model_view'),
    path('vehicle_dead_axle_model/<int:pk>', directory_vehicle_dead_axle_model_view, name='directory_vehicle_dead_axle_model_view'),
    path('vehicle_clients_model/<int:pk>', directory_clients_model_view, name='directory_clients_model_view'),
    path('vehicle_service_provider/<int:pk>', directory_vehicle_service_provider_view, name='directory_vehicle_service_provider_view'),

]