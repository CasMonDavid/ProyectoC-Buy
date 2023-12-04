from django.contrib import messages
from django.shortcuts import render, redirect
from usuarios.form import formulario_Login_Usuario, formulario_Registro_Usuario
from django.contrib.auth import authenticate, login

# Create your views here.
def login_form(request):
    form = formulario_Login_Usuario()
    if request.method == 'POST':
        form = formulario_Login_Usuario(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuario y/o contraseña incorrectos')
            
    cxt = {"form": form}
    return render(request, 'usuarios/InicioDeSesion.html', cxt)

def registro_form(request):
    form = formulario_Registro_Usuario()
    if request.method == 'POST':
        form = formulario_Registro_Usuario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos correctamente almacenados')
    cxt1 = {"form": form}
    return render(request, 'usuarios/Registro.html', cxt1)
