from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(label='Clave', max_length=100, widget=forms.PasswordInput)

class SignupForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    username = forms.CharField(label='Usuario', max_length=100)
    email = forms.CharField(label='Email', max_length=100, widget=forms.EmailInput)
    password = forms.CharField(label='Clave', max_length=100, widget=forms.PasswordInput)


class AdminSignupForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    username = forms.CharField(label='Usuario', max_length=100)
    email = forms.CharField(label='Email', max_length=100, widget=forms.EmailInput)
    password = forms.CharField(label='Clave', max_length=100, widget=forms.PasswordInput)
    isStaff = forms.BooleanField(label="Es staff", required=False)

class CreateEstadioForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    descripción = forms.CharField(widget=forms.Textarea)

class CreateTipoAsientoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=200)
    costo = forms.FloatField(label='Costo')
    capacidad = forms.IntegerField(label='Capacidad')
    descripción = forms.CharField(widget=forms.Textarea)

#Cambios
# class CreateEventoForm(forms.Form):
#     fecha_hora = forms.CharField(label='Fecha')
#     equipo1 = forms.CharField(label='Equipo2')
#     equipo2 = forms.CharField(label='Equipo1')
#     tipo = forms.CharField(label = 'Tipo De Partido')
#Fin Cambios

class CreatePartidoForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    inicio = forms.DateTimeField(label="Inicio", widget=forms.widgets.DateInput(attrs={'type': 'datetime-local', 'placeholder': '2021-01-01 00:00'}))
    fin = forms.DateTimeField(label="Fin", widget=forms.widgets.DateInput(attrs={'type': 'datetime-local', 'placeholder': '2021-01-01 01:00'}))
