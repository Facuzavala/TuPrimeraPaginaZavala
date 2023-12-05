from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def inicio(request):
    return render (request, 'inicio.html')

def registro(request):
    return render(request, 'registro.html')
def socios(request):
    nombre = "Facundo"
    return render(request, 'socios.html', {
        'nombre' : nombre 
    })
def entradas(request):
    return render(request, 'entradas.html')
def cuotaMensual(request):
    return render(request, 'cuotaMensual.html')
def grupoFamiliar(request):
    return render(request, 'grupoFamiliar.html')

def registro_formulario(request):
    if request.method == "POST":
        miformulario_regis = RegistroFormulario(request.POST)
        print(miformulario_regis)
        if miformulario_regis.is_valid:
            info_regis= miformulario_regis.cleaned_data
            registro = Registro(info_regis["nro_socio"], info_regis["clave"])
            registro.save()
        return render (request,'inicio.html')
    else:
        miformulario_regis = RegistroFormulario()
        return render(request, 'registro_formulario.html', {"miformulario_regis": miformulario_regis})

entradas
def entradas_formulario(request):
    if request.method == "POST":
        miformulario_entradas = EntradasFormulario(request.POST)
        print(miformulario_entradas)
        if miformulario_entradas.is_valid:
            info_entradas = miformulario_entradas.cleaned_data
            entradas = Entradas(info_entradas["partido"], info_entradas["ubicacion"],info_entradas["valor"])
            entradas.save()
        return render (request,'inicio.html')
    else:
        miformulario_entradas = EntradasFormulario()
        return render(request, 'entradas_formulario.html', {"miformulario_entradas": miformulario_entradas})

def socios_formulario(request):
    if request.method == "POST":
        miformulario_socio = SociosFormulario(request.POST)
        print(miformulario_socio)
        if miformulario_socio.is_valid:
            info_socio = miformulario_socio.cleaned_data
            socios = Socios(info_socio["nro_socio"], info_socio["clave"])
            socios.save()
        return render (request,'inicio.html')
    else:
        miformulario_socio = SociosFormulario()
        return render(request, 'socios_formulario.html', {"miformulario_socio": miformulario_socio})

def buscar_socio(request):
    return render(request, "RiverPlate/buscar_socio.html")

def buscar(request):
    respuesta = f"Estoy buscando al socio nro: {request.GET["socio"]}"

    return HttpResponse(respuesta)



