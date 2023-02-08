from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import *
from .forms import VehicleForm


def index(request):
    vehicles = Vehicle.objects.all
    return render(request, 'service_portal/index.html', {'vehicles': vehicles})


def directory_vehicle_model_view(request, pk):
    vehicle_models = DirectoryVehicleModel.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryVehicleModel.html', {'vehicle_models': vehicle_models})
# def directory_vehicle_model_view(request):
#     vehicle_models = DirectoryVehicleModel.objects.all
#     return render(request, 'service_portal/DirectoryVehicleModel.html', {'vehicle_models': vehicle_models})


def directory_vehicle_engine_model_view(request, pk):
    vehicle_engine_models = DirectoryVehicleEngineModel.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryVehicleEngineModel.html', {'vehicle_engine_models': vehicle_engine_models})


def directory_vehicle_transmission_model_view(request, pk):
    vehicle_transmission_models = DirectoryVehicleTransmissionModel.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryVehicleTransmissionModel.html', {'vehicle_transmission_models': vehicle_transmission_models})


def directory_vehicle_live_axle_model_view(request, pk):
    vehicle_live_axle_models = DirectoryVehicleLiveAxleModel.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryVehicleLiveAxleModel.html', {'vehicle_live_axle_models': vehicle_live_axle_models})


class VehicleCreateView(CreateView):
    template_name = 'service_portal/create.html'
    form_class = VehicleForm
    success_url = reverse_lazy('index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pass
