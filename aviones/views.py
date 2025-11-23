from django.shortcuts import render, redirect, get_object_or_404
from .models import Avion
from .forms import AvionForm

def lista_aviones(request):
    aviones = Avion.objects.all()
    return render(request, 'aviones.html', {'aviones': aviones})

def agregar_avion(request):
    if request.method == 'POST':
        form = AvionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_aviones')
    else:
        form = AvionForm()
    return render(request, 'agregar_avion.html', {'form': form})

def editar_avion(request, pk):
    avion = get_object_or_404(Avion, pk=pk)
    if request.method == 'POST':
        form = AvionForm(request.POST, instance=avion)
        if form.is_valid():
            form.save()
            return redirect('lista_aviones')
    else:
        form = AvionForm(instance=avion)
    return render(request, 'editar_avion.html', {'form': form})

def eliminar_avion(request, pk):
    avion = get_object_or_404(Avion, pk=pk)
    if request.method == 'POST':
        avion.delete()
        return redirect('lista_aviones')
    return render(request, 'eliminar_avion.html', {'avion': avion})