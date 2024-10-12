# matriculas/models.py
from django.db import models
from estudiantes_cursos.models import EstudiantesCursos

class Matriculas(models.Model):
    ESTADO_CHOICES = [
        ('En espera de pago', 'En espera de pago'),
        ('Pago', 'Pago'),
        ('Finalizada', 'Finalizada'),
    ]
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    fecha_inicio = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    estudiante_curso = models.ForeignKey(EstudiantesCursos, on_delete=models.SET_NULL, null=True, related_name='matriculas')
    
    def __str__(self):
    # Usamos format para agregar separadores de miles.
        return f"Matricula ID: {self.id} - Costo: {self.costo:,.2f}"


    #def __str__(self):
        #return f"Matricula ID: {self.id} - Estudiante en Curso: {self.estudiante_curso}"

    class Meta:
        db_table = 'matriculas'

