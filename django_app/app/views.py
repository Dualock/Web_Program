from django.http import HttpResponse
from django.shortcuts import render

from .models import Estadio

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def estadios(request):
    estadios_disponibles = Estadio.objects.all
    context = {
        'estadios_disponibles': estadios_disponibles
    }
    return render(request, 'estadios.html', context)

def estadio(request, estadio_id):
    info_estadio = Estadio.objects.get(id=estadio_id)
    print(info_estadio)
    context = {
        'estadio': info_estadio
    }
    return render(request, 'estadio.html', context)
