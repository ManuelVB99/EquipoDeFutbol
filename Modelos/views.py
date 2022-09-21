from django.shortcuts import render
from django.http import HttpResponse
from Modelos.models import Equipo_Tecnico
from Modelos.forms import *

# Create your views here.

def home(request):
    return render(request, "home.html")

def equipo(request):
    if request.method == "POST":
       equipo =  form_equipo(request.POST)
       if equipo.is_valid():
        info = equipo.cleaned_data
        equipo_tec = Equipo_Tecnico(nombre = request.POST['nombre'], apellido = request.POST['apellido'], edad = request.POST['edad'], funcion = request.POST["funcion"])
        equipo_tec.save()
        return render(request, "Equipo.html")
    else:
        equipo = form_equipo()
    return render(request, "Equipo.html", {"equipo": equipo})