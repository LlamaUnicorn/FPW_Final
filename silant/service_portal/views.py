from django.shortcuts import render
from django.views.generic import CreateView

from .models import Vehicle
from .forms import VehicleForm


def index(request):
    vehicles = Vehicle.objects.all
    return render(request, 'service_portal/index.html', {'vehicles': vehicles})


class VehicleCreateView(CreateView):
    template_name = 'service_portal/create.html'
    form_class = VehicleForm
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['']