from django.urls import path

from .views import index, VehicleCreateView, directory_vehicle_model_view

urlpatterns = [
    path('create/', VehicleCreateView.as_view(), name='create'),
    path('', index, name='index'),
    path('vehicle_model/', directory_vehicle_model_view, name='directory_vehicle_model_view'),
]