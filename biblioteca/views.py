from django.http import HttpResponse
from .models import Libro
from rest_framework.decorators import api_view
from rest_framework.response import Response

def resumen(request):
  total = Libro.objects.count()
  return HttpResponse(f"Actualmente hay {total} libros registrados en la biblioteca.")

@api_view(['GET'])
def listado_libros(request):
    libros = Libro.objects.all()
    datos = [
        {
            "id": libro.id,
            "titulo": libro.titulo,
            "autor": libro.autor.nombre,
            "precio": libro.precio,
            "disponible": libro.disponible,
        }
        for libro in libros
    ]
    return Response(datos)
