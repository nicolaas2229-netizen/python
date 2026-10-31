from django.db import models

class Curso(models.Model):
  nombre = models.CharField(max_length=100)
  def __str__(self):
    return self.nombre

class Estudiante(models.Model):
  nombre = models.CharField(max_length=100)
  apellido = models.CharField(max_length=100)
  curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True, related_name='estudiantes')
  def __str__(self):
    return f"{self.nombre} {self.apellido}"
