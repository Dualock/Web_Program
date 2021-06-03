from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, contra):
        self.nombre = nombre
        self.contra = contra

def Say_Hi(request): #First View
    links = ["Estadios", "Partidos", "Perfil"]
    p1 = Persona("dualock", "webprogram1234")
    fecha = datetime.datetime.now()
    #doc_template1 = loader.get_template('template.html')
    '''Importa la plantilla template desde la carpeta templates, para esto
    ir a settings.py y agregar a Dir la direccion donde estan los templates'''
    #ctx = Context({"usuario": p1.nombre, "clave": p1.contra , "fecha": fecha, "links":links} )
    #documento = doc_template1.render({"usuario": p1.nombre, "clave": p1.contra , "fecha": fecha, "links":links})
    #return HttpResponse(documento)
    '''Importa la plantilla template desde la carpeta templates, para esto
    ir a settings.py y agregar a Dir la direccion donde estan los templates,
    lo renderiza y lo muestra'''
    return render(request, "template.html",{"usuario": p1.nombre, "clave": p1.contra , "fecha": fecha, "links":links} )
