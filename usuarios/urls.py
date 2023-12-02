from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('InicioDeSesion/', views.login_form, name='inicioDeSesion_usuario'),
    path('Registro/', views.registro_form, name='registro_Usuario')
]