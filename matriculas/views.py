from django.shortcuts import render
from .models import Matriculas

def matriculas(request):
    
    matriculas = Matriculas.objects.all();
    
    return render(request, 'matriculas.html', {
        'title': 'Lista de matriculas',
        'matriculas': matriculas
    })
    