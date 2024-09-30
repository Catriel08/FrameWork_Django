from django.contrib import admin
from .models import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "apellidos", "dni", "telefono", "email", "fecha_nacimiento", "rol")
    list_filter = ("rol",)


