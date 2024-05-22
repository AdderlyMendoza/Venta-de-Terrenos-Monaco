from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProyectoForm, SubProyectoForm

# Create your views here.

def app_proyectos(request):
    return render(request, 'proyectos/app_proyectos.html')


def listar_proyectos(request):
    proyectos = Proyectos.objects.all()
    return render(request, 'proyectos/listar_proyectos.html' , {'proyectos': proyectos})

def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyectos:listar_proyectos')
        
    else:
        form = ProyectoForm()
    return render(request, 'proyectos/crear_proyecto.html', {'form': form})

def ver_proyecto(request, pk):
    proyecto = get_object_or_404(Proyectos, id=pk)
    return render(request, 'proyectos/ver_proyecto.html', {'proyecto': proyecto})

def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyectos, id=pk)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyectos:listar_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'proyectos/editar_proyecto.html', {'form': form})




def eliminar_proyecto(request, pk):  
    proyecto = get_object_or_404(Proyectos, id=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('proyectos:listar_proyectos')
    return render(request, 'proyectos/eliminar_proyecto.html', {'proyecto': proyecto})


    #subproyectos


def proyectos_y_subproyectos(request):
    proyectos = Proyectos.objects.all()
    proyecto_seleccionado = None
    subproyectos = None

    if 'proyecto_id' in request.GET:
        proyecto_id = request.GET['proyecto_id']
        proyecto_seleccionado = get_object_or_404(Proyectos, pk=proyecto_id)
        subproyectos = obtener_subproyectos(proyecto_seleccionado)  # Función para obtener subproyectos actualizados

    return render(request, 'proyectos/subproyectos/subproyectos.html', {'proyectos': proyectos, 'proyecto_seleccionado': proyecto_seleccionado, 'subproyectos': subproyectos})




def obtener_subproyectos(proyecto):
    return Sub_Proyecto.objects.filter(proyecto=proyecto)



def crear_subproyecto(request):
    if request.method == 'POST':
        form = SubProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            subproyecto = form.save(commit=False)
            subproyecto.proyecto = form.cleaned_data['proyecto']  # Asigna el proyecto seleccionado al subproyecto
            subproyecto.save()
            return redirect('proyectos:subproyectos')
    else:
        form = SubProyectoForm()
    return render(request, 'proyectos/subproyectos/crear_subproyecto.html', {'form': form})

def actualizar_subproyecto(request, pk):
    subproyecto = get_object_or_404(Sub_Proyecto, id=pk)
    if request.method == 'POST':
        form = SubProyectoForm(request.POST, instance=subproyecto)
        if form.is_valid():
            form.save()
            return redirect('proyectos:subproyectos')
    else:
        form = SubProyectoForm(instance=subproyecto)
    return render(request, 'proyectos/subproyectos/actualizar_subproyecto.html', {'form': form})


def eliminar_subproyecto(request, pk):
    subproyecto = get_object_or_404(Sub_Proyecto, id=pk)
    
    if request.method == 'POST':
        subproyecto.delete()
        return redirect('proyectos:subproyectos')
    
    return render(request, 'proyectos/subproyectos/eliminar_subproyecto.html', {'subproyecto': subproyecto})

# filter SUBproyect
