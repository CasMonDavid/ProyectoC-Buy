from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('InicioDeSesion/', views.login_form, name='inicioDeSesion_usuario'),
    path('Registro/', views.registro_form, name='registro_Usuario'),
    path('CerrarSesion/', LogoutView.as_view, name='cerrarSesion_usuario'),
    path('Configuracion/', views.configuracionUsuario_form, name='configuracion_usuario')
]

# metodo para subir imagenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)