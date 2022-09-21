from django.shortcuts import render
from Modelos.models import *
from django.http import HttpResponse

def jugadores(request):
    if request.method == "POST":
       jugadores =  Jugadores(nombre = request.POST['nombre'], apellido = request.POST['apellido'], edad = request.POST['edad'], posicion = request.POST["posicion"], pieHabil = request.POST["pieHabil"])
       jugadores.save()
       jugadores = Jugadores.objects.all()
       return render(request, "Jugadores.html", {"Jugadores": jugadores})
    jugadores = Jugadores.objects.all()
    return render(request, "Jugadores.html", {"Jugadores": jugadores})

def buscar_jugador(request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        jugador = Jugadores.objects.filter(apellido__icontains = apellido)
        return render(request, "Jugadores.html", {"jugador": jugador})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)