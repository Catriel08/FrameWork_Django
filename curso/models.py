from django.db import models
from persona.models import Persona
from django.core.exceptions import ValidationError

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad_maxima = models.IntegerField(null=False)
    profesor = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)
    
    #def save(self, *args, **kwargs):
        #self.full_clean()
        #super().save(*args, **kwargs)
        
    #def clean(self):
        #if self.capacidad_maxima <= 0:
            #raise ValidationError('La capacidad máxima debe ser mayor a 0.')

        
    def __str__(self):
        return self.nombre
        
    #def __str__(self) -> str:
        #return f'{self.nombre} - {self.capacidad_maxima} - {self.profesor.nombre} - {self.profesor.apellidos}'
        
    #def __str__(self):
        #return f'{self.nombre} - Capacidad: {self.capacidad_maxima} - Profesor: {self.profesor}'
        
    class Meta:
        db_table = 'Curso'
