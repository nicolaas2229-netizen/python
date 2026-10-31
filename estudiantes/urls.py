from django.urls import path
from estudiantes import views

urlpatterns = [
    path('', views.resumen, name="resumen_estudiantes"),
    path('resumen/', views.resumen, name='resumen_estudiantes'),
    path('api/estudiantes/', views.listado_estudiantes, name='api_estudiantes'),
]