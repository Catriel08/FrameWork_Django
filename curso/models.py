from django.db import models
from persona.models import Persona

class Curso (models.Model):
    nombre=models.CharField(max_length=100)
    capacidad_maxima=models.IntegerField(null=False)
    profesor_id=models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f'{self.nombre} - {self.capacidad_maxima} - {self.profesor_id}'
    
class Meta:
        db_table='Curso'
