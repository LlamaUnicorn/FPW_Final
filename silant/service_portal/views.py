from django.shortcuts import render

from .models import Vehicle


def index(request):
    vehicles = Vehicle.objects.all
    return render(request, 'service_portal/index.html', {'vehicles': vehicles})
