from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, ListView, DeleteView, CreateView
from .models import Curso
from persona.models import Persona
from django.contrib import messages
from django.urls import reverse, reverse_lazy

class ListCursosView(ListView):
    model = Curso
    template_name = 'curso.html'
    context_object_name = 'curso'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Cursos'
        return context

    def get_queryset(self):
        return Curso.objects.all()
    
class CreateCursoView(CreateView):
    model = Curso
    fields = ['nombre', 'capacidad_maxima', 'profesor']
    template_name = 'curso_nuevo.html'

    def get(self, request, *args, **kwargs):
        profesores = Persona.objects.filter(rol='Profesor')
        return render(request, self.template_name, {
            'title': 'Agregar Curso Nuevo',
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
        messages.success(request, f"El curso {nombre} ha sido creado correctamente")
        return redirect('cursos')
    
    
class GestionarCursoView(UpdateView):
    model = Curso
    template_name = 'gestionar-curso.html'
    fields = ['nombre', 'capacidad_maxima', 'profesor']
    context_object_name = 'curso'
    success_url = reverse_lazy('cursos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Gestionar Curso'
        context ['is_update'] = True
        context['profesores'] = Persona.objects.filter(rol='Profesor')
        return context
    
    def post(self, request, *args, **kwargs):
        if 'update' in request.POST:
            messages.success(request, "Curso actualizado correctamente.")
        elif 'delete' in request.POST:
            self.object = self.get_object()
            self.object.delete()
            messages.success(request, "Curso eliminado correctamente.")
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)
