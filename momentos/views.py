from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'momentos/Inicio.html')

def carrito_form(request):
    return render(request, 'momentos/Carrito.html')

def busqueda_form(request):
    return render(request, 'momentos/ResultadoBusqueda.html')

def informacionProducto_form(request):
    return render(request, 'momentos/InformacionProducto.html')