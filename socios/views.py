from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from django.db.models import Sum, F
from django.http import HttpResponseBadRequest
from .forms import *

# Create your views here.
def app_socios(request):
    return render(request, 'socios/app_socios.html')


class SocioListView(ListView):
    model = Socio
    template_name = 'socios/socio_list.html'

class SocioDetailView(DetailView):
    model = Socio
    template_name = 'socios/socio_detail.html'

class SocioCreateView(CreateView):
    model = Socio
    fields = ['estado', 'documento', 'nombre', 'ap_paterno', 'ap_Materno', 'celular']
    template_name = 'socios/socio_form.html'
    success_url = reverse_lazy('socios:socio_list')

class SocioUpdateView(UpdateView):
    model = Socio
    fields = ['estado', 'documento', 'nombre', 'ap_paterno', 'ap_Materno', 'celular']
    template_name = 'socios/socio_form.html'
    success_url = reverse_lazy('socios:socio_list')

class SocioDeleteView(DeleteView):
    model = Socio
    template_name = 'socios/socio_confirm_delete.html'
    success_url = reverse_lazy('socios:socio_list')




#inversion

def listar_inversiones(request):
    inversiones = Inversion.objects.all()
    return render(request, 'socios/inversion/listar_inversion.html', {'inversiones': inversiones})


def crear_inversion(request):
    if request.method == 'POST':
        form = InversionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('socios:listar_inversiones')
    else:
        form = InversionForm()
    return render(request, 'socios/inversion/crear_inversion.html', {'form': form})


def actualizar_inversion(request, inversion_id):
    inversion = get_object_or_404(Inversion, pk=inversion_id)
    if request.method == 'POST':
        form = InversionForm(request.POST, instance=inversion)
        if form.is_valid():
            form.save()
            return redirect('socios:listar_inversiones')
    else:
        form = InversionForm(instance=inversion)
    return render(request, 'socios/inversion/actualizar_inversion.html', {'form': form})


def eliminar_inversion(request, inversion_id):
    inversion = get_object_or_404(Inversion, pk=inversion_id)
    if request.method == 'POST':
        inversion.delete()  # Llama al método delete() en la instancia 'inversion'
        return redirect('socios:listar_inversiones')
    return render(request, 'socios/inversion/eliminar_inversion.html', {'inversion': inversion})



def detalle_inversion(request, inversion_id):
    inversion = get_object_or_404(Inversion, pk=inversion_id)
    total_ganancias_acumuladas = inversion.cantidad_invertida * inversion.porcentaje_ganancia / 100
    return render(request, 'socios/inversion/detalle_inversion.html', {'inversion': inversion, 'total_ganancias_acumuladas': total_ganancias_acumuladas})

