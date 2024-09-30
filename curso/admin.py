from django.contrib import admin
from .models import Curso
from persona.models import Persona

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "capacidad_maxima", "profesor")
    

