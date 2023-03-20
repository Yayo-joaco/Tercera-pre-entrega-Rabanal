from django.urls import path
from AppCoder.views import cursos, estudiantes, profesores


urlpatterns = [
    path('cursos', cursos),
    path('estudiantes', estudiantes),
    path('profesores', profesores),
]