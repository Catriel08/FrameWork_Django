from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def hola_mundo(request):
    return render (request, 'prueba.html')
