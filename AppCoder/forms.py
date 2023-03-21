from django import forms

class CursoForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)
    camada = forms.IntegerField(min_value=1000)

class EstudiantesForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class EntregableForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha_de_entrega = forms.DateField()
    entregado = forms.BooleanField()

class BusquedaCursoForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)