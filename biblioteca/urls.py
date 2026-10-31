from django.urls import path
from biblioteca import views

urlpatterns = [
    path('', views.resumen, name="resumen"),
    path('resumen/', views.resumen, name='resumen'),
    path('api/libros/', views.listado_libros, name='api_libros'),
]