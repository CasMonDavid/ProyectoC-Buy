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
            username1 = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username1, password=password)
            if user is not None:
                login(request, user)
                request.session['sesionUsuario'] = username1
                request.session.modified = True
                nomUsuario = request.session.get('sesionUsuario', 'N/A')
                messages.success(request, 'Bienvenido usuario: '+nomUsuario)
                return redirect('momentos:home')
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
        else:
            messages.error(request, 'Datos ingresados no validos')
    cxt1 = {"form": form}
    return render(request, 'usuarios/InicioDeSesion.html', cxt1)

def configuracionUsuario_form(request):
    return render(request, 'usuarios/ConfiguracionPerfil.html')