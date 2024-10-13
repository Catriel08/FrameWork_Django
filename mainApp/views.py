from django.shortcuts import render
from django.views.generic import ListView, CreateView

def inicio(request):
    return render(request, 'inicio.html')
