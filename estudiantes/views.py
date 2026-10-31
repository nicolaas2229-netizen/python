from django.http import HttpResponse
from .models import Estudiante
from rest_framework.decorators import api_view
from rest_framework.response import Response

def resumen(request):
  total = Estudiante.objects.count()
  return HttpResponse(f"Actualmente hay {total} estudiantes registrados.")

@api_view(['GET'])
def listado_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    datos = [
        {
            "id": e.id,
            "nombre": e.nombre,
            "apellido": e.apellido,
            "curso": e.curso.nombre if e.curso else None,
        }
        for e in estudiantes
    ]
    return Response(datos)
