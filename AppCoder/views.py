from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse



# Create your views here.
def cursos(request):
    return render(request, "index.html")

def estudiantes(request):
    pass

def profesores(request):
    pass
