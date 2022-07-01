

from .views import  carga_familares, inicio, saludo, lista_familiares,index
from django.urls import path, include


urlpatterns = [

    path('', inicio),
    path('saludo/<nombre>/<apellido>', saludo),
    path('carga_familiares/<nombre_persona>/<edad_persona>/<fecha_persona>', carga_familares),
    path('lista_familiares/',lista_familiares),
    path('index/',index),

]
