from django.shortcuts import render, get_object_or_404
from .models import Auto

def home(request):
    busqueda = request.GET.get('buscar')
    if busqueda:
        autos = Auto.objects.filter(modelo__icontains=busqueda)

    else:
        autos = Auto.objects.all()
    return render(request, 'catalogo/index.html', {'autos': autos, 'busqueda': busqueda})

def detalle(request, auto_id):
    auto = get_object_or_404(Auto, pk=auto_id)
    return render(request, 'catalogo/detalle_auto.html', {'auto': auto})