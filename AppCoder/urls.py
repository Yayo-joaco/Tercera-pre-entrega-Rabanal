from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path('', inicio , name = "AppCoderInicio"),
    path('cursos', cursos , name = "AppCoderCursos"),
    path('buscar_curso', busqueda, name = "AppCoderBuscarCursos"),
    path('estudiantes', estudiantes, name = "AppCoderEstudiantes"),
    path('profesores', profesores , name = "AppCoderProfesores"),
    path('entregables', entregables , name = "AppCoderEntregables"),
]