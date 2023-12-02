from django.shortcuts import render
from usuarios.form import formulario_Login_Usuario, formulario_Registro_Usuario

# Create your views here.
def login_form(request):
    form = formulario_Login_Usuario()
    cxt = {"form": form}
    return render(request, 'usuarios/InicioDeSesion.html', cxt)

def registro_form(request):
    form = formulario_Registro_Usuario()
    if request.method == 'POST':
        form = formulario_Registro_Usuario(request.POST)
        if form.is_valid():
            form.save()
    cxt1 = {"form": form}
    return render(request, 'usuarios/Registro.html', cxt1)