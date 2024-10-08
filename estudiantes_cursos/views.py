from django.shortcuts import render
from .models import EstudiantesCursos

def estudianteCurso(request):
    
    estudianteCurso = EstudiantesCursos.objects.all();
    
    return render(request, 'estudiante_curso.html', {
        'title': 'Matricula de estudiante por curso',
        'estudiantes_cursos': estudianteCurso
    })
