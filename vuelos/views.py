from django.shortcuts import render, redirect, get_object_or_404
from .models import Vuelo
from .forms import VueloForm

def lista_vuelos(request):
    vuelos = Vuelo.objects.all()
    return render(request, 'vuelos.html', {'vuelos': vuelos})

def agregar_vuelo(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vuelos')
    else:
        form = VueloForm()
    return render(request, 'agregar_vuelo.html', {'form': form})

def editar_vuelo(request, pk):
    vuelo = get_object_or_404(Vuelo, pk=pk)
    if request.method == 'POST':
        form = VueloForm(request.POST, instance=vuelo)
        if form.is_valid():
            form.save()
            return redirect('lista_vuelos')
    else:
        form = VueloForm(instance=vuelo)
    return render(request, 'editar_vuelo.html', {'form': form})

def eliminar_vuelo(request, pk):
    vuelo = get_object_or_404(Vuelo, pk=pk)
    if request.method == 'POST':
        vuelo.delete()
        return redirect('lista_vuelos')
    return render(request, 'eliminar_vuelo.html', {'vuelo': vuelo})