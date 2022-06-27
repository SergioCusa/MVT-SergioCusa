from .views import  carga_familares, inicio, saludo, lista_familiares
from django.urls import path, include


urlpatterns = [

    path('', inicio),
    path('saludo/<nombre>/<apellido>', saludo),
    path('carga_familiares/<nombre_persona>/<edad_persona>', carga_familares),
    path('lista_familiares/',lista_familiares)

]
