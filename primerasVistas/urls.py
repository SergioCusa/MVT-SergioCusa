

from .views import  carga_familares, inicio, saludo, lista_familiares,index
from django.urls import path, include


urlpatterns = [

    path('', inicio, name="index"),
    path('saludo/<nombre>/<apellido>', saludo),
    path('carga_familiares/', carga_familares,name="carga_familiares"),
    path('lista_familiares/',lista_familiares, name="lista_familiares"),
    path('index/',index),

]
 