from django import forms
from .models import Vehicle


class VehicleFilterForm(forms.Form):
    vehicle_serial_number = forms.CharField(label='Заводской номер', max_length=100, required=False)
    fields = ['__all__']

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)


class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
