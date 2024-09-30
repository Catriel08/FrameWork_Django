from django.db import models

class Persona (models.Model):
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    dni=models.CharField(max_length=10)
    telefono=models.CharField(max_length=10)
    email=models.EmailField()
    fecha_nacimiento=models.DateField()
    rol=models.CharField(max_length=20)
    create_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellidos}'
    
class Meta:
        db_table='persona'