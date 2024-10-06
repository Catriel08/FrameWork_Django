from django.contrib import admin
from estudiantes_cursos.models import EstudiantesCursos

@admin.register(EstudiantesCursos)
class EstudiantesCursosAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'fecha_inicio', 'fecha_final', 'estado', 'nota_final')
