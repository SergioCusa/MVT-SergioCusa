

from pyexpat import model
from django.db import models

# Create your models here.

class Persona (models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha=models.DateField(null=True)
     

    
