from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, ListView, DeleteView, CreateView
from .models import Curso
from persona.models import Persona

class ListCursosView(ListView):
    model = Curso
    template_name = 'curso.html'
    context_object_name = 'curso'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de cursos'
        return context

    def get_queryset(self):
        return Curso.objects.all()
    
class CreateCursoView(CreateView):
    model = Curso
    template_name = 'curso_nuevo.html'

    def get(self, request, *args, **kwargs):
        profesores = Persona.objects.filter(rol='Profesor')
        return render(request, self.template_name, {
            #'title': 'Agregar curso nuevo',
            'profesores': profesores
        })

    def post(self, request, *args, **kwargs):
        
        nombre = request.POST.get('nameTextInput')
        capacidad_maxima = request.POST.get('capacidadTextInput')
        profesor_id = request.POST.get('profesorSelect')

        profesor = Persona.objects.get(id=profesor_id)

        cursos = Curso(
            nombre=nombre,
            capacidad_maxima=capacidad_maxima,
            profesor=profesor
        )

        cursos.save()
        return redirect('cursos')