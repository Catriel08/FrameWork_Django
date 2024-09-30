from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Persona

def get_estudiantes(request):
    
    estudiantes= Persona.objects.filter(rol='Estudiante');
    #seles * from persona
    
    return render(request, 'lista-estudiantes.html', {
        'title': 'Lista de Estudiantes',
        'estudiantes': estudiantes
    })
    


# Create your views here.
