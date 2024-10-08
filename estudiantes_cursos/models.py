from django.db import models
from persona.models import Persona
from curso.models import Curso

class EstudiantesCursos(models.Model):
    estudiante = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, related_name='cursos', limit_choices_to={'rol': 'Estudiante'})
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, related_name='estudiantes')
    fecha_inicio = models.DateField()
    fecha_final = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=50)
    nota_final = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def __str__(self):
        return f"Estudiante: {self.estudiante} - Curso: {self.curso}"
    
    class Meta:
        db_table = 'Estudiantes_cursos'
