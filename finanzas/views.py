from django.shortcuts import render

# Create your views here.
def app_finanzas(request):
    return render(request, 'finanzas/app_finanzas.html')