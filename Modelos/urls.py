from django.urls import path
from Modelos.views import *

urlpatterns = [
    path("Jugadores/", jugadores),
    path("buscar_jugadores/", buscar_jugador),
    path("Fechas/", fechas),
    path("Equipo/", equipo),
    path("buscar_equipo/", buscar_equipo)
]