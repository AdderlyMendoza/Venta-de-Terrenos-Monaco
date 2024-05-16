from django.shortcuts import render, redirect
from .models import Cliente
from django.shortcuts import get_object_or_404
from .forms import *
# from web.models import *


from django.shortcuts import render



def app_clientes(request):
    return render(request, 'clientes/app_clientes.html')

def clientes(request):
    lista_clientes = Cliente.objects.all()
    data = {
        'lista_clientes' :lista_clientes,
    }
    return render(request, 'clientes/clientes.html', data)

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:clientes')
        
    else:
        form = ClienteForm()
    return render(request, 'clientes/crear_cliente.html', {'form': form})

def ver_cliente(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    return render(request, 'clientes/ver_cliente', {'cliente': cliente})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes:clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form})

def eliminar_cliente(request, pk):  
    cliente = get_object_or_404(Cliente, id=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes:listar_proyectos')
    return render(request, 'clientes/eliminar_cliente.html', {'cliente': cliente})


# SEPARAR LOTES

# def listar_ventas(request):
#     ventas = Venta.objects.all()
#     return render(request, 'clientes/lotes/lista_ventas.html', {'ventas': ventas})
#     web = Web.objects.all()
#     return render(request, 'web/listar_compras.html', {'web':web})

def listar_ventas(request):
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




def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            try:
                venta = form.save(commit=False)
                venta.save()

                subproyecto = venta.subproyecto
                subproyecto.estado = 'SEPARADO'
                subproyecto.save()
                return redirect('clientes:listar_ventas')
            except ValueError as e:
                error_message = str(e)
                return render(request, 'clientes/lotes/crear_venta.html', {'form': form, 'error_message': error_message})
    else:
        form = VentaForm()  # Instancia el formulario sin ningún argumento adicional

    return render(request, 'clientes/lotes/crear_venta.html', {'form': form})

def ver_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    return render(request, 'clientes/lotes/ver_venta.html', {'venta': venta})

def actualizar_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('listar_ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'clientes/lotes/actualizar_venta.html', {'form': form})

def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    if request.method == 'POST':
        venta.delete()
        return redirect('listar_ventas')
    return render(request, 'clientes/lotes/confirmar_eliminar_venta.html', {'venta': venta})

