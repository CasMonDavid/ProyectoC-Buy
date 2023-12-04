from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Esta clase "form" en python es solo para modificar la apariencia de los formularios en html: InicioDeSesion.html

class formulario_Login_Usuario(forms.Form):
    username = forms.EmailField(label='Correo email:', widget=forms.TextInput(attrs={'class': 'clasevacia'}))
    password = forms.CharField(label='Contraseña:', widget=forms.PasswordInput(attrs={'class': 'clasevacia'}))

class formulario_Registro_Usuario(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'subtitle'}))
    first_name = forms.CharField(label='Nombre(s)', widget=forms.TextInput(attrs={'class': 'subtitle'}))
    email = forms.CharField(label='Correo electronico:', widget=forms.EmailInput(attrs={'class': 'subtitle'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'subtitle'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class': 'subtitle'}))
    cellphone = forms.CharField(label='Número celular', widget=forms.NumberInput(attrs={'class': 'subtitle'}))
    direccion = forms.CharField(label='Dirección de envio', widget=forms.Textarea(attrs={'class': 'subtitle'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name']