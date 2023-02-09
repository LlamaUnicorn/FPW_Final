from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.shortcuts import redirect

from service_portal.permissions import IsManagerUser, IsServiceUser
from service_portal.models import Vehicle
from service_portal.serializers.vehicle_serializer import VehicleSerializer, VehicleManagersSerializer, VehicleServiceSerializer

from .models import *
from .forms import VehicleFilterForm
from .filters import VehicleFilter


# def index(request):
#     vehicles = Vehicle.objects.all
#     return render(request, 'service_portal/index.html', {'vehicles': vehicles})
def index(request):
    form = VehicleFilterForm(request.GET)
    vehicles = Vehicle.objects.all()
    if form.is_valid():
        vehicle_serial_number = form.cleaned_data['vehicle_serial_number']
        if vehicle_serial_number:
            vehicles = vehicles.filter(vehicle_serial_number__icontains=vehicle_serial_number)
    return render(request, 'service_portal/index.html', {'vehicles': vehicles, 'form': form})


def directory_vehicle_model_view(request, pk):
    vehicle_models = DirectoryVehicleModel.objects.filter(pk=pk)
    return render(request, 'service_portal/DirectoryVehicleModel.html', {'vehicle_models': vehicle_models})


# def directory_vehicle_model_view(request):
#     vehicle_models = DirectoryVehicleModel.objects.all
#     return render(request, 'service_portal/DirectoryVehicleModel.html', {'vehicle_models': vehicle_models})


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


class VehicleCreateView(CreateView):
    template_name = 'service_portal/create.html'
    form_class = VehicleFilterForm
    success_url = reverse_lazy('index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pass


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
# class VehicleList(ListView):
#     model = Vehicle
#     ordering = 'vehicle_shipping_date'
#     template_name = 'index.html'
#     context_object_name = 'vehicles'
#
#     def get_queryset(self):
#         queryset = super.get_queryset()
#         self.filterset = VehicleFilter(self.request.GET, queryset)
#         return self.filterset.qs
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filterset'] = self.filterset
#         return context
#
#
# class VehicleDetail(DetailView):
#     model = Vehicle
#     template_name = 'index.html'
#     context_object_name = 'vehicle'

# def vehicle_list(request):
#     form = VehicleFilterForm(request.GET)
#     if form.is_valid():
#         vehicle_serial_number = form.cleaned_data['vehicle_serial_number']
#         if vehicle_serial_number:
#             vehicles = Vehicle.objects.filter(vehicle_serial_number__exact=vehicle_serial_number)
#         else:
#             vehicles = Vehicle.objects.all()
#     else:
#         vehicles = Vehicle.objects.all()
#     return render(request, 'vehicle_list.html', {'vehicles': vehicles, 'form': form})