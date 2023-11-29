from django.urls import path
from . import views

urlpatterns = [
    path('InicioDeSesion/', views.login_form, name='inicioDeSesion_usuario')
]