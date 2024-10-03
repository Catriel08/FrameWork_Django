from django.contrib import admin
from .models import Curso
from persona.models import Persona

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "capacidad_maxima", "profesor")
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "profesor":
            kwargs["queryset"] = Persona.objects.filter(rol='Profesor')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
