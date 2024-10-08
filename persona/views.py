from django.shortcuts import render,redirect
from django.views.generic import View, UpdateView, ListView, DeleteView, CreateView
from .models import Persona


class ListEstudiantesView(ListView):
    def get(self, request, *args, **kwargs):
        estudiantes= Persona.objects.filter(rol='Estudiante')
    
        return render(request, 'lista-estudiantes.html', {
            'title': 'Lista de Estudiantes',
            'estudiantes': estudiantes, }) 


class CreateEstudiantesView(CreateView):
    model = Persona
    #fields = ['nombre', 'apellidos', 'dni', 'telefono', 'email', 'fecha_nacimiento']

    def get(self, request, *args, **kwargs):
        return render(request, 'form-create-estudiantes.html')

    def post(self, request, *args, **kwargs):
        nombre = request.POST.get('nameTextInput')
        apellido = request.POST.get('lastNameTextInput')
        dni = request.POST.get('dniTextInput')
        telefono = request.POST.get('telTextInput')
        email = request.POST.get('inputEmail')
        fecha_nacimiento = request.POST.get('birthdateInput')

        persona = Persona(
            nombre=nombre,
            apellidos=apellido,
            dni=dni,
            telefono=telefono,
            email=email,
            fecha_nacimiento=fecha_nacimiento,
            rol='Estudiante'
        )

        persona.save()
        return redirect('lista-estudiantes')
            
        #return render(request, 'form-create-estudiantes.html')
        
