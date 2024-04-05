from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')


def acerca_de_mi(request):
    return render(request, 'acerca_de_mi.html')


def contactame(request):
    return render(request, 'contactame.html')


def servicios(request):
    return render(request, 'servicios.html')
