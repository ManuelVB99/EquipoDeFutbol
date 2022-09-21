from django import forms

class form_equipo(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    funcion = forms.CharField(max_length=30)