from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Esta clase "form" en python es solo para modificar la apariencia de los formularios en html: InicioDeSesion.html

class formulario_Login_Usuario(forms.Form):
    username = forms.CharField(label='Nombre de usuario:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class formulario_Registro_Usuario(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Nombre(s)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Correo electronico:', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    cellphone = forms.CharField(label='Número celular', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(label='Dirección de envio', widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name']

