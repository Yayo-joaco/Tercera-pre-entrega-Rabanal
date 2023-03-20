from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.
def guardar_curso(request, camada):
    curso = Curso(nombre="Python", camada=camada)
    curso.save()
    return HttpResponse("usuario creado exitosamente")

