from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def app_rrhh(request):
    return render(request, 'rrhh/app_rrhh.html')


def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'rrhh/listar_empleados.html', {'empleados': empleados})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rrhh:listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'rrhh/crear_empleado.html', {'form': form})

def actualizar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, id=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('rrhh:listar_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'rrhh/actualizar_empleado.html', {'form': form})

def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, id=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('rrhh:listar_empleados')
    return render(request, 'rrhh/eliminar_empleado.html', {'empleado': empleado})