from django.shortcuts import render

from .models import Sensors


def index(request):
    sensors = Sensors.objects.get(id=1)
    pressure = sensors.pressure
    temperature = sensors.temperature
    depth = sensors.depth
    context = {
        'pressure': pressure,
        'temperature': temperature,
        'depth': depth,
    }
    return render(request, 'display_sensors/index.html', context)
