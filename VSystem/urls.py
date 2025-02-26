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
from mainApp.views import inicio
from persona.views import ListEstudiantesView,ListProfesoresView, CreateEstudiantesView, CreateProfesoresView, GestionarEstudianteView, GestionarProfesorView
from curso.views import ListCursosView, CreateCursoView, GestionarCursoView
from matriculas.views import ListMatriculaView, CreateMatriculaVew, GestionarMatriculaView
from estudiantes_cursos.views import ListEstudianteCurso, CreateEstudianteCurso, GestionarEstudianteCurso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('lista-estudiantes/', ListEstudiantesView.as_view(), name='lista-estudiantes'),
    path("lista-profesores/", ListProfesoresView.as_view(), name="lista-profesores"),
    
    path('lista-cursos/',ListCursosView.as_view(), name='cursos'),
    path('agregar-curso/', CreateCursoView.as_view(), name='agregar-curso'),
    path('gestionar-curso/<int:pk>/', GestionarCursoView.as_view(), name="gestionar-curso"),
    
    path('crear-estudiante/', CreateEstudiantesView.as_view(), name='form-create-estudiantes'),
    path("crear-profesor/", CreateProfesoresView.as_view(), name="form-create-profesores"),
    path('gestionar-estudiante/<int:pk>/', GestionarEstudianteView.as_view(), name='gestionar-estudiante'),
    path('gestionar-profesor/<int:pk>/', GestionarProfesorView.as_view(), name='gestionar-profesor'),

    path('matriculas/', ListMatriculaView.as_view(), name='matriculas'),
    path("crear-matricula/", CreateMatriculaVew.as_view(), name="crear-matricula"),
    path("gestionar-matricula/<int:pk>", GestionarMatriculaView.as_view(), name="gestionar-matriculas"),
    
    path('estudiante-curso/', ListEstudianteCurso.as_view(), name='estudiante-curso'),
    path('crear-estudiante_curso/', CreateEstudianteCurso.as_view(), name='crear-estudiantes_cursos'),
    path("gestionar-estudiante_curso/<int:pk>/", GestionarEstudianteCurso.as_view(), name="gestionar-estudiantes_cursos"),
    path('eliminar-estudiante_curso/<int:pk>/', GestionarEstudianteCurso.as_view(), name='eliminar-estudiante-curso'),
]
