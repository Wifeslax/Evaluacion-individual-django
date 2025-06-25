from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def inicio(request):
    return render(request, 'paginas/inicio.html')

def acerca(request):
    return render(request, 'paginas/acerca.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')

