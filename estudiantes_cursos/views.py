from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import EstudiantesCursos
from persona.models import Persona
from curso.models import Curso
from django.contrib import messages


class ListEstudianteCurso(ListView):
    model = EstudiantesCursos
    template_name = 'estudiante_curso.html'
    context_object_name = 'estudiantes_cursos'
    success_url = reverse_lazy('estudiante-curso')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inscripción de Estudiantes en Cursos'
        return context
    

class CreateEstudianteCurso(CreateView):
    model = EstudiantesCursos
    fields = ['estudiante', 'curso', 'fecha_inicio', 'fecha_final', 'estado', 'nota_final']
    template_name = 'crear-estudiante_curso.html'
    success_url = reverse_lazy('estudiante-curso')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = Persona.objects.filter(rol='Estudiante')
        context['cursos'] = Curso.objects.all()
        context['title'] = 'Crear Inscripción de Estudiante en Curso'
        return context

    def post(self, request, *args, **kwargs):
        estudiante_id = request.POST.get('estudiante')
        curso_id = request.POST.get('curso')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_final = request.POST.get('fecha_final')
        estado = request.POST.get('estado')
        
        if estado == 'En Curso':
            nota_final = 0.0
        else:
            nota_final = request.POST.get('nota_final', 0.0)

        # Obtener la instancia del estudiante y del curso usando su id
        estudiante = Persona.objects.get(id=estudiante_id)
        curso = Curso.objects.get(id=curso_id)

        estudiantes_cursos = EstudiantesCursos(
            estudiante=estudiante,
            curso=curso,
            fecha_inicio=fecha_inicio,
            fecha_final=fecha_final,
            estado=estado,
            nota_final=nota_final
        )

        estudiantes_cursos.save()
        messages.success(request, f"La inscripción de {estudiantes_cursos.estudiante} en el curso {estudiantes_cursos.curso} ha sido creada correctamente.")
        return redirect('estudiante-curso')
    

class GestionarEstudianteCurso(UpdateView):
    model = EstudiantesCursos
    fields = ['estudiante', 'curso', 'fecha_inicio', 'fecha_final', 'estado', 'nota_final']
    template_name = 'gestionar-estudiante_curso.html'
    context_object_name = 'estudiantes_cursos'
    success_url = reverse_lazy('estudiante-curso')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = Persona.objects.filter(rol='Estudiante')
        context['cursos'] = Curso.objects.all()
        context['title'] = 'Gestionar Inscripción de Estudiante en Curso'
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        if 'update' in request.POST:
            # Se controla que el estado no se modifique si es "Finalizado"
            if self.object.estado == 'Finalizado':
                request.POST._mutable = True  # Me permite la modificación del objeto QueryDict, por defecto vienen como iinmutables o False
                request.POST['estado'] = self.object.estado  # Restablecer el estado actual
                request.POST._mutable = False  # Vuelve a establecer como inmutable
            
            form = self.get_form()
            if form.is_valid():
                self.object = form.save()
                messages.success(request, "Inscripción actualizada correctamente.")
                return self.form_valid(form)
            else:
                messages.error(request, "Hubo un error al actualizar la inscripción.")
        
        elif 'delete' in request.POST:
            self.object.delete()
            messages.success(request, "Inscripción eliminada correctamente.")
            return redirect(self.success_url)

        return self.form_invalid(form)
