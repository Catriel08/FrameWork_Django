"""
URL configuration for VSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainApp.views import inicio, hola_mundo
from persona.views import get_estudiantes
from curso.views import curso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,  name='inicio'),
    path('lista-estudiantes/',get_estudiantes, name='lista-estudiantes'),
    path('prueba/', hola_mundo, name='prueba'),
    path('lista-cursos/',curso, name='cursos'),
]
