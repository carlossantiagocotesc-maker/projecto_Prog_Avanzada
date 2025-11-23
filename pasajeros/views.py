from django.shortcuts import render, redirect, get_object_or_404
from .models import Pasajero
from .forms import PasajeroForm

def lista_pasajeros(request):
    pasajeros = Pasajero.objects.all()
    return render(request, 'pasajeros.html', {'pasajeros': pasajeros})

def agregar_pasajero(request):
    if request.method == 'POST':
        form = PasajeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pasajeros')
    else:
        form = PasajeroForm()
    return render(request, 'agregar_pasajero.html', {'form': form})

def editar_pasajero(request, pk):
    pasajero = get_object_or_404(Pasajero, pk=pk)
    if request.method == 'POST':
        form = PasajeroForm(request.POST, instance=pasajero)
        if form.is_valid():
            form.save()
            return redirect('lista_pasajeros')
    else:
        form = PasajeroForm(instance=pasajero)
    return render(request, 'editar_pasajero.html', {'form': form})

def eliminar_pasajero(request, pk):
    pasajero = get_object_or_404(Pasajero, pk=pk)
    if request.method == 'POST':
        pasajero.delete()
        return redirect('lista_pasajeros')
    return render(request, 'eliminar_pasajero.html', {'pasajero': pasajero})