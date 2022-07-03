


from pipes import Template
from re import template
from django.http import HttpResponse
from primerasVistas.forms import formPersona
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
    
    # nombre= request.POST.get("nombre")
    # edad=request.POST.get("edad")
    # fecha=request.POST.get("fecha")
    
    # persona= Persona(nombre=nombre,edad=edad,fecha=fecha)
    # persona.save()
    
    form_persona= formPersona()
    
    return render (request,"carga_familiares.html",{"form":form_persona })
  

def lista_familiares(request):
    
    template= loader.get_template("lista_familiares.html",)
    
    lista_familiares=Persona.objects.all()
    
    render= template.render({"lista_familiares":lista_familiares})
    
    return HttpResponse(render)

def index(request):
    
    return render(request,"index.html")