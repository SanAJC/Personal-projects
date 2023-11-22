from django.db import models

# Create your models here.

class Asistencia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(max_length=100, verbose_name="Email")
    numero_telefonico = models.CharField(max_length=10, verbose_name="Número Telefónico")
    materia = models.CharField(max_length=100, verbose_name="Materia")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    
    class Meta:
        verbose_name='Asistencia'
        verbose_name_plural='Asistencias'
        
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

