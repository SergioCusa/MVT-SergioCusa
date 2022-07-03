from django import forms

class formPersona (forms.Form):
    nombre=forms.CharField(max_length=30)
    edad=forms.IntegerField()
    fecha=forms.DateField()
         