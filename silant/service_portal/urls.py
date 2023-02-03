from django.urls import path

from .views import index, VehicleCreateView

urlpatterns = [
    path('create/', VehicleCreateView.as_view(), name='create'),
    path('', index, name='index'),
]