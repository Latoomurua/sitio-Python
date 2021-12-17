from os import close
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
import datetime

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segundaView(request):
    return HttpResponse("Soy Lautaro Murua este es mi sitio web desarrollado en Django")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: <br> {dia}"

    return HttpResponse(documentoDeTexto)

def apellido(request, ape):
    return HttpResponse(f"El mejor programador se llama {ape}!!")

def probandoTemplate(request):

    mejorProgramador = "Lautaro Murua"
    lenguaje = "Python"
    frameworksPython = ["flask", "Pyramid", "Django", "Web2py"]

    diccionario = {"nombre":mejorProgramador,"lenguaje":lenguaje, "frameworks": frameworksPython}

    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)