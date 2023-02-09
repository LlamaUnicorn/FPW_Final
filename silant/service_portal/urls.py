from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *
from . import views
from service_portal.views import VehicleDetailView, VehicleManagersDetailView, VehicleServiceDetailView

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
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicle-managers/<int:pk>/', VehicleManagersDetailView.as_view(), name='vehicle-managers-detail'),
    path('vehicle-service/<int:pk>/', VehicleServiceDetailView.as_view(), name='vehicle-service-detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logout_view, name='logout'),
]
