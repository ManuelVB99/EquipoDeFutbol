from django.urls import path
from Modelos.views import *

urlpatterns = [
   
    path("Equipo/", equipo),
    path("home/", home),
 
    
]