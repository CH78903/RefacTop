om django.shortcuts import render, get_object_or_404
from .models import Auto

def home(request):
    busqueda = request.GET.get('buscar')
    if busqueda:
        autos = Auto.objects.filter(modelo__icontains=busqueda)