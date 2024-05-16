from django.shortcuts import render, redirect
from .models import *
from .forms import formularioWeb
# Create your views here.

def appWeb(request):
    return render(request, "web/web.html")
        

def separar_lote(request):
    if request.method=='POST':
        form = formularioWeb(request.POST)
        if form.is_valid():
            form.save()
            return redirect("web:pag_web") # redd a una pag que diga que ya se separo xd
    else:
        form = formularioWeb()

        # Obtener solo los valores de la columna 'terrenos' desde la base de datos
        # terrenos = Web.objects.values_list('terrenos', flat=True)
              
    # return render(request, "web/separar_lote.html", {'form': form, 'terrenos': terrenos}) # enviamos el form y los terrenos
    return render(request, "web/separar_lote.html", {'form': form}) # enviamos el form y los terrenos


def listar(request):
    web = Web.objects.all()
    return render(request, 'web/listar_compras.html', {'web':web})

def pag_web(request):
    return render(request, 'web/pag_web.html')