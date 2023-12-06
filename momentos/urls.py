from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index
from . import views

app_name = "momentos"

urlpatterns = [
    path('Casa/', views.index, name='home'),
    path('Carrito/', views.carrito_form, name='carrito_usuario'),
    path('Resultado/', views.busqueda_form, name='resultadoBusqueda'),
    path('Resultado/Detalles/', views.informacionProducto_form, name='detallesProducto'),
    path('eliminar/<int:id_prod>/', views.eliminar_producto, name='eliminar'),
    path('vaciar/', views.eliminar_todos_productos, name='vaciar'),
    path('comprar/', views.confirmar_compra, name='comprar')
]

# metodo para subir imagenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)