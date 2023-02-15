from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from service_portal.permissions import IsManagerUser, IsServiceUser
from service_portal.serializers.vehicle_serializer import VehicleSerializer, VehicleManagersSerializer, VehicleServiceSerializer

from .models import *
from .forms import VehicleFilterForm, VehicleCreateForm


def index(request):
    form = VehicleFilterForm(request.GET)
    vehicles = Vehicle.objects.all()
    if form.is_valid():
        vehicle_serial_number = form.cleaned_data['vehicle_serial_number']
        if vehicle_serial_number:
            vehicles = vehicles.filter(vehicle_serial_number__icontains=vehicle_serial_number)
    return render(request, 'service_portal/index.html', {'vehicles': vehicles, 'form': form})


@login_required
def authorized_index_view(request):
    form = VehicleFilterForm(request.GET)
    vehicles = Vehicle.objects.all()
    if form.is_valid():
        vehicle_serial_number = form.cleaned_data['vehicle_serial_number']
        if vehicle_serial_number:
            vehicles = vehicles.filter(vehicle_serial_number__icontains=vehicle_serial_number)
    return render(request, 'service_portal/auth_index.html', {'vehicles': vehicles, 'form': form})


@login_required
def vehicle_view(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'service_portal/vehicle_view.html', {'vehicles': vehicles})


@login_required
def service_view(request):
    services = Service.objects.all()
    return render(request, 'service_portal/service_view.html', {'services': services})


@login_required
def reclamation_view(request):
    reclamations = Reclamation.objects.all()
    return render(request, 'service_portal/reclamation_view.html', {'reclamations': reclamations})


def directory_vehicle_model_view(request, pk):
    vehicle_models = DirectoryVehicleModel.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryVehicleModel.html', {'vehicle_models': vehicle_models})


def directory_vehicle_engine_model_view(request, pk):
    vehicle_engine_models = DirectoryVehicleEngineModel.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryVehicleEngineModel.html',
                  {'vehicle_engine_models': vehicle_engine_models})


def directory_vehicle_transmission_model_view(request, pk):
    vehicle_transmission_models = DirectoryVehicleTransmissionModel.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryVehicleTransmissionModel.html',
                  {'vehicle_transmission_models': vehicle_transmission_models})


def directory_vehicle_live_axle_model_view(request, pk):
    vehicle_live_axle_models = DirectoryVehicleLiveAxleModel.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryVehicleLiveAxleModel.html',
                  {'vehicle_live_axle_models': vehicle_live_axle_models})


def directory_vehicle_dead_axle_model_view(request, pk):
    vehicle_dead_axle_models = DirectoryVehicleDeadAxleModel.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryVehicleDeadAxleModel.html',
                  {'vehicle_dead_axle_models': vehicle_dead_axle_models})


def directory_clients_model_view(request, pk):
    vehicle_clients_models = DirectoryClientsModel.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryClientsModel.html',
                  {'vehicle_clients_models': vehicle_clients_models})


def directory_vehicle_service_provider_view(request, pk):
    vehicle_service_providers = DirectoryServiceProvider.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryServiceProvider.html',
                  {'vehicle_service_providers': vehicle_service_providers})


def directory_service_types_view(request, pk):
    service_service_types = DirectoryServiceType.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryServiceTypes.html',
                  {'service_service_types': service_service_types})


def directory_reclamation_malfunction_type_view(request, pk):
    directory_malfunction_types = DirectoryMalfunctionType.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryMalfunctionType.html',
                  {'directory_malfunction_types': directory_malfunction_types})


def directory_reclamation_repair_type_view(request, pk):
    directory_reclamation_repair_types = DirectoryMalfunctionType.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryReclamationRepairType.html',
                  {'directory_reclamation_repair_types': directory_reclamation_repair_types})


class VehicleCreateView(CreateView):
    template_name = 'service_portal/create.html'
    form_class = VehicleCreateForm
    success_url = reverse_lazy('auth_index')


class VehicleUpdateView(UpdateView):
    template_name = 'service_portal/UpdateVehicle.html'
    form_class = VehicleCreateForm
    success_url = reverse_lazy('auth_index')
    model = Vehicle

    def get_object(self, queryset=None):
        return Vehicle.objects.get(pk=self.kwargs.get('pk'))


class VehicleDeleteView(DeleteView):
    template_name = 'service_portal/DeleteVehicle.html'
    model = Vehicle
    success_url = reverse_lazy('auth_index')

    def get_object(self, queryset=None):
        return Vehicle.objects.get(pk=self.kwargs.get('pk'))


class VehicleDetailView(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleManagersDetailView(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleManagersSerializer


class VehicleServiceDetailView(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleServiceSerializer


class VehicleManagersView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleManagersSerializer
    permission_classes = [IsAuthenticated, IsManagerUser]
    template_name = 'service_portal/vehicle_managers.html'


class VehicleServiceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleServiceSerializer
    permission_classes = [IsAuthenticated, IsServiceUser]
    template_name = 'service_portal/vehicle_service.html'


def logout_view(request):
    logout(request)
    return redirect('login')
