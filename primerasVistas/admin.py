from django.contrib import admin
from django.db import models

# Register your models here.

class Persona (models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha=models.DateField(null=True)
     