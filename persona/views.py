from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Persona

def get_estudiantes(request):
    
    estudiantes= Persona.objects.filter(rol='Estudiante');
    #seles * from persona
    
    return render(request, 'lista-estudiantes.html', {
        'title': 'Lista de Estudiantes',
        'estudiantes': estudiantes
    })

def fromCreateEstudiante(request):
    if request.method =="POST":
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
        
    return render(request, 'form-create-persona.html')
        
