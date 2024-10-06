from django.shortcuts import render
from .models import EstudiantesCursos

def estudianteCurso(request):
    
    estudianteCurso = EstudiantesCursos.objects.all();
    
    return render(request, 'estudiante_curso.html', {
        'title': 'Me la juego un 90% a que está MAL XD',
        'estudiantes_cursos': estudianteCurso
    })
