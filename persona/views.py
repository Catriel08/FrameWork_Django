from django.shortcuts import render,redirect
from django.views.generic import View, UpdateView, ListView, DeleteView, CreateView
from .models import Persona
from django.contrib import messages
from django.urls import reverse


class CreatePersonaView(CreateView):
    model = Persona
    fields = ['nombre', 'apellidos', 'dni', 'telefono', 'email', 'fecha_nacimiento']
    template_name = 'form-create-persona.html'
    rol = None

    def get_context_data(self, **kwargs):
        # Agregar el rol y título al contexto
        context = super().get_context_data(**kwargs)
        context['rol'] = self.rol
        context['title'] = self.title
        return context

    def post(self, request, *args, **kwargs):
        nombre = request.POST.get('nameTextInput')
        apellidos = request.POST.get('lastNameTextInput')
        dni = request.POST.get('dniTextInput')
        telefono = request.POST.get('telTextInput')
        email = request.POST.get('inputEmail')
        fecha_nacimiento = request.POST.get('birthdateInput')
        rol = request.POST.get('rol') 

        persona = Persona(
            nombre=nombre,
            apellidos=apellidos,
            dni=dni,
            telefono=telefono,
            email=email,
            fecha_nacimiento=fecha_nacimiento,
            rol=rol
        )

        persona.save()
        messages.success(request, f"{rol} {nombre} {apellidos} ha sido creado correctamente.")
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse(self.success_url) # Redirige a la url
        #return render(request, 'form-create-estudiantes.html')

class ListEstudiantesView(ListView):
    template_name = 'lista-estudiantes.html'
    context_object_name = 'estudiantes'

    def get_queryset(self):
        return Persona.objects.filter(rol='Estudiante')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Estudiantes'
        return context
        

class ListProfesoresView(ListView):
    template_name = 'lista-profesores.html'
    context_object_name = 'profesores'

    def get_queryset(self):
        return Persona.objects.filter(rol='Profesor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Profesores'
        return context


class CreateEstudiantesView(CreatePersonaView):
    template_name = 'form-create-persona.html'
    success_url = 'lista-estudiantes'
    rol = 'Estudiante'
    title = 'Agregar Estudiante'
    

class CreateProfesoresView(CreatePersonaView):
    template_name = 'form-create-persona.html'
    success_url = 'lista-profesores'
    rol = 'Profesor'
    title = 'Agregar Profesor'

            
        
