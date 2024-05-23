from django.shortcuts import render, redirect
from .models import *
from proyectos.models import Sub_Proyecto
from .forms import formularioWeb

from django.shortcuts import get_object_or_404


# Create your views here.

def appWeb(request):
    return render(request, "web/web.html")
        

# def separar_lote(request):
#     if request.method=='POST':
#         form = formularioWeb(request.POST)
        
#         datos = request.POST["terrenos"] # TERRENOS SEPARADOS POR EL USUARIO
#         lista_datos = datos.split(", ")
#         for dato in lista_datos:
#             print(dato)
#             try:
#                 # Buscar el registro por el valor de nombre
#                 objeto = get_object_or_404(Sub_Proyecto, nombre=dato)
                
#                 # Cambiar el valor de estado
#                 objeto.estado = "SEPARADO"
                
#                 # Guardar los cambios en la base de datos
#                 objeto.save()
            
#             except Sub_Proyecto.DoesNotExist:
#                 pass

#         if form.is_valid():
#             form.save()
#             return redirect("web:pag_web") # redd a una pag que diga que ya se separo xd
#     else:
#         form = formularioWeb()

#         # Obtener solo los valores de la columna 'terrenos' desde la base de datos
#         # terrenos = Web.objects.values_list('terrenos', flat=True)
              
#     # return render(request, "web/separar_lote.html", {'form': form, 'terrenos': terrenos}) # enviamos el form y los terrenos
#     return render(request, "web/separar_lote.html", {'form': form}) # enviamos el form y los terrenos

def separar_lote(request):
    if request.method == 'POST':
        form = formularioWeb(request.POST)
        
        if form.is_valid():
            form.save()
            
            datos = request.POST.get("terrenos", "")  # Obtener los terrenos separados por el usuario
            print("###############################################")
            print(datos)
            print("###############################################")

            lista_datos = [dato.strip() for dato in datos.split(",")]  # Separar los terrenos y eliminar espacios en blanco
            
            for dato in lista_datos:
                try:
                    subproyecto = Sub_Proyecto.objects.get(nombre=dato)
                    subproyecto.estado = "SEPARADO"
                    subproyecto.save()
                except Sub_Proyecto.DoesNotExist:
                    print(f"El terreno '{dato}' no existe en la base de datos.")
            
            return redirect("web:pag_web")  # Redirigir a una página que confirme que se realizó la separación
    else:
        form = formularioWeb()

        terrenos = Web.objects.values_list('terrenos', flat=True)
        estados = list(Sub_Proyecto.objects.values_list('estado', flat=True))

    
    #return render(request, "web/separar_lote.html", {'form': form})
    return render(request, "web/separar_lote.html", {'form': form, 'terrenos': terrenos, 'estados': estados}) # enviamos el form y los terrenos


def listar(request):
    web = Web.objects.all()
    return render(request, 'web/listar_compras.html', {'web':web})

def pag_web(request):
    return render(request, 'web/pag_web.html')

def cambiar_estado_subproyecto(terrenoCambiar):
    try:
        # Buscar el registro por el valor de nombre
        objeto = get_object_or_404(Sub_Proyecto, nombre=terrenoCambiar)
        
        # Cambiar el valor de estado
        objeto.estado = "SEPARADO"
        
        # Guardar los cambios en la base de datos
        objeto.save()
        
        # Retornar el objeto actualizado
        return None
    
    except Sub_Proyecto.DoesNotExist:
        # Retornar None si no se encuentra el terreno
        return None