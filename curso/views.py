from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Curso
    
def curso(request):
    
    cursos = Curso.objects.all();
    
    return render(request, 'curso.html', {
        'title': 'Lista de Cursos',
        'curso': cursos
    })
    
    
