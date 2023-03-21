from django.shortcuts import render, redirect
from AppCoder.models import Curso, Estudiantes, Profesor, Entregable
from AppCoder.forms import CursoForm, EstudiantesForm, ProfesorForm, EntregableForm, BusquedaCursoForm
from django.http import HttpResponse


def cursos(request):

    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_save = Curso(
                nombre = informacion['nombre'],
                camada = informacion['camada']
            )
            curso_save.save()
        return redirect("AppCoderInicio")

    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos,
        "form": CursoForm(),
    }
    return render(request, "AppCoder/cursos.html", context = context)

def estudiantes(request):

    if request.method == "POST":
        mi_formulario = EstudiantesForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            estudiantes_save = Estudiantes(
                nombre = informacion['nombre'],
                apellido = informacion['apellido'],
                email = informacion['email']
            )
            estudiantes_save.save()
        return redirect("AppCoderInicio")

    all_estudiantes = Estudiantes.objects.all()
    context = {
        "estudiantes": all_estudiantes,
        "form": EstudiantesForm()
    }
    return render(request, "AppCoder/estudiantes.html", context = context)

def profesores(request):

    if request.method == "POST":
        mi_formulario = ProfesorForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor_save = Profesor(
                nombre = informacion['nombre'],
                apellido = informacion['apellido'],
                email = informacion['email'],
                profesion = informacion['profesion']
            )
            profesor_save.save()
        return redirect("AppCoderInicio")

    all_profesor = Profesor.objects.all()
    context = {
        "profesor": all_profesor,
        "form": ProfesorForm()
    }
    return render(request, "AppCoder/profesores.html", context = context)

def entregables(request):
    if request.method == "POST":
        mi_formulario = EntregableForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            entregable_save = Entregable(
                nombre=informacion['nombre'],
                fecha_de_entrega=informacion['fecha_de_entrega'],
                entregado=informacion['entregado'],
            )
            entregable_save.save()
        return redirect("AppCoderInicio")

    all_entregables = Entregable.objects.all()
    context = {
        "entregable": all_entregables,
        "form": EntregableForm()
    }
    return render(request, "AppCoder/entregables.html", context=context)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def busqueda(request):
    context = {}
    mi_formulario = BusquedaCursoForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        cursos_filtrados = Curso.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "cursos": cursos_filtrados,
            "form_busqueda": BusquedaCursoForm()
        }

    return render(request, "AppCoder/inicio.html", context = context)
