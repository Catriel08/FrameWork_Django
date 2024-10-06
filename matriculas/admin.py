from django.contrib import admin
from matriculas.models import Matriculas

@admin.register(Matriculas)
class MatriculasAdmin(admin.ModelAdmin):
    list_display = ('estado', 'fecha_inicio', 'costo', 'estudiante_curso')

