from django.http import HttpResponse
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