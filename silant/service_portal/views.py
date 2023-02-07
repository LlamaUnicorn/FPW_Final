from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Vehicle, DirectoryVehicleModel
from .forms import VehicleForm


def index(request):
    vehicles = Vehicle.objects.all
    return render(request, 'service_portal/index.html', {'vehicles': vehicles})


def directory_vehicle_model_view(request):
    vehicle_models = DirectoryVehicleModel.objects.all
    return render(request, 'service_portal/DirectoryVehicleModel.html', {'vehicle_models': vehicle_models})



class VehicleCreateView(CreateView):
    template_name = 'service_portal/create.html'
    form_class = VehicleForm
    success_url = reverse_lazy('index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pass
