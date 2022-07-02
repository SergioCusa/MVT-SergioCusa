


from pipes import Template
from re import template
from django.http import HttpResponse
from primerasVistas.models import Persona
from django.template import Template, loader 
from django.shortcuts import render


def inicio (request):
    
    template=loader.get_template("inicio.html")
    
    render=template.render()
    
    return HttpResponse (render)
    
def saludo (request,nombre,apellido):
    return HttpResponse(f"Hola {nombre} {apellido}") 

def carga_familares(request):
    
    
    # persona=Persona(nombre=nombre_persona,edad=edad_persona,fecha=fecha_persona)
    # persona.save()
    
    return render (request,"carga_familiares.html",{})
  

def lista_familiares(request):
    
    template= loader.get_template("lista_familiares.html",)
    
    lista_familiares=Persona.objects.all()
    
    render= template.render({"lista_familiares":lista_familiares})
    
    return HttpResponse(render)

def index(request):
    
    return render(request,"index.html")