from django.shortcuts import render, redirect
from .models import Matriculas
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from .models import EstudiantesCursos
from django.contrib import messages

class ListMatriculaView(ListView):
    model = Matriculas
    template_name = 'matriculas.html'
    context_object_name = 'matriculas'
    success_url = reverse_lazy('matriculas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Lista Matriculas'
        return context
    
class CreateMatriculaVew(CreateView):
    model = Matriculas
    fields = ['estado', 'fecha_inicio', 'costo', 'estudiante_curso']
    template_name = 'crear-matricula.html'
    success_url = reverse_lazy('matriculas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['estudiante_curso'] = EstudiantesCursos.objects.all()
        context ['title'] = 'Nueva Matricula'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Matricula añadida correctamente')
        return super().form_valid(form)
    
    
class GestionarMatriculaView(UpdateView):
    model = Matriculas
    fields = ['estado', 'fecha_inicio', 'costo', 'estudiante_curso']
    template_name = 'gestionar-matriculas.html'
    context_object_name = 'matriculas'
    success_url = reverse_lazy('matriculas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiante_curso'] = EstudiantesCursos.objects.all()
        context['title'] = 'Gestionar Matricula'
        return context
    
    def post(self, request, *args, **kwargs):
        if 'update' in request.POST:
            messages.success(request, "Matrícula actualizada correctamente.")
        elif 'delete' in request.POST:
            self.object = self.get_object()
            self.object.delete()
            messages.success(request, "Matrícula eliminada correctamente.")
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)

    