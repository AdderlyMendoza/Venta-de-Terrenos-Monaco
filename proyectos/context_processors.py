from .models import Proyectos


def proyectos_processor(request):
    proyectos = Proyectos.objects.all()
    return {
        'proyectos': proyectos
    }
