from django.shortcuts import redirect, render, get_list_or_404
from django.contrib.auth.models import User
from usuarios.models import customUsuario
from .models import carrito_usuario, carrito_producto, historial_usuario, Producto
from django.db import transaction


# Create your views here.
def index(request):
    return render(request, 'momentos/Inicio.html')

def carrito_form(request):
    username_actual = request.session.get('sesionUsuario', 'NoAplica')

    if username_actual != 'NoAplica':
        try:
            usuario_actual = User.objects.get(username=username_actual)
        except User.DoesNotExist:
            print(f'El cliente no existe con el username= {username_actual}')

    paramId_pro = request.GET.get('id')

    if paramId_pro is not None and usuario_actual != 'NoAplica':
        try:
            carrito_creado = carrito_usuario.objects.get(id_usuario=usuario_actual.id, esta_completado=False)
            
            if paramId_pro is not None:
                producto_por_id = Producto.objects.get(id=int(paramId_pro))
                try:
                    carrito_actual = carrito_producto.objects.filter(id_compra_id=carrito_creado, esta_completado=False)
                    noExiste = True # variable que checa si el producto ya esta en el carrito, si no esta lo mete nuevo | si ya esta solo lo modifica sin crear ninguno nuevo
                    totalAPagar=0

                    for productoEnCarrito in carrito_actual:

                        totalAPagar =+productoEnCarrito.total_precio # reune la cantidad total SOLO EN BD

                        if productoEnCarrito.id_producto == producto_por_id:
                            totalDeEseProducto = productoEnCarrito.cantidad_pro+1
                            precio = productoEnCarrito.total_precio+producto_por_id.precio
                            noExiste = False

                            totalAPagar =+producto_por_id.precio

                            with transaction.atomic():
                                productoEnCarrito.cantidad_pro = totalDeEseProducto
                                productoEnCarrito.total_precio = precio
                                productoEnCarrito.save()
                    if noExiste:
                        compraProductos = carrito_producto(
                            id_compra = carrito_creado,
                            id_producto = producto_por_id,
                            cantidad_pro = 1,
                            total_precio = producto_por_id.precio
                        )
                        compraProductos.save()

                    carrito_lista_compra = list(carrito_actual)

                    return render(request, 'momentos/Carrito.html', {'CarritoDeCompra':carrito_lista_compra, 'totalPago':totalAPagar}) # manda contexto
                
                except carrito_producto.DoesNotExist:
                    print(f'El carrito de productos no existe con el id= {carrito_creado.id_compra}')
                    compraProductos = carrito_producto(
                        id_compra = carrito_creado,
                        id_producto = producto_por_id,
                        cantidad_pro = 1,
                        total_precio = producto_por_id.precio
                    )
                    compraProductos.save()
        except carrito_usuario.DoesNotExist:
            print(f'el carrito no existe con el id= {usuario_actual.id}')
            carrito = carrito_usuario(
                id_usuario = usuario_actual
            )
            carrito.save()
    else:
        if usuario_actual is not None:
            try:
                carrito_creado = carrito_usuario.objects.get(id_usuario=usuario_actual.id, esta_completado=False)
                try:
                    carrito_actual = carrito_producto.objects.filter(id_compra=carrito_creado, esta_completado=False)
                    producto_por_id = Producto.objects.all()
                    totalAPagar=0

                    for productoEnCarrito in carrito_actual:

                        totalAPagar += productoEnCarrito.total_precio # reune la cantidad total SOLO EN BD

                        #for proSelect in producto_por_id:
                        #    if productoEnCarrito.id_producto == proSelect.id:
                        #        totalAPagar =+ proSelect.precio

                    carrito_lista_compra = list(carrito_actual)

                    return render(request, 'momentos/Carrito.html', {'CarritoDeCompra':carrito_actual, 'totalPago':totalAPagar}) # manda contexto

                except carrito_producto.DoesNotExist:
                    print(f'El carrito de productos no existe con el id= {carrito_creado.id_compra}')
                    compraProductos = carrito_producto(
                        id_compra = carrito_creado,
                        id_producto = producto_por_id,
                        cantidad_pro = 1,
                        total_precio = producto_por_id.precio
                    )
                    compraProductos.save()
            except carrito_usuario.DoesNotExist:
                print(f'el carrito no existe con el id= {usuario_actual.id}')
                carrito = carrito_usuario(
                        id_usuario = usuario_actual
                    )
                carrito.save()

    return render(request, 'momentos/Carrito.html') # lo manda sin contexto

def eliminar_producto(request, id_prod):
    carrito_eliminar = carrito_producto.objects.get(id_compra_producto=id_prod).delete()
    return redirect("momentos:carrito_usuario")

def confirmar_compra(request):
    username_actual = request.session.get('sesionUsuario', 'NoAplica')

    if username_actual != 'NoAplica' :
        try:
            usuario_actual = User.objects.get(username=username_actual)
            try:
                carrito_creado = carrito_usuario.objects.get(id_usuario=usuario_actual, esta_completado=False)
                try:
                    carrito_actual = carrito_producto.objects.filter(id_compra=carrito_creado, esta_completado=False)
                    for producto in carrito_actual:
                        producto.esta_completado = True
                        producto.save()

                except carrito_usuario.DoesNotExist:
                    print(f'El carrito con los productos no existe= {carrito_creado.id_compra}')
                historial = historial_usuario(
                    id_usuario = usuario_actual,
                    id_compra = carrito_creado
                )
                historial.save()
                carrito_creado.esta_completado = True
                carrito_creado.save()
            except carrito_usuario.DoesNotExist:
                print(f'El cliente aun no tiene carrito= {usuario_actual.username}')
        except User.DoesNotExist:
            print(f'El cliente no existe con el username= {username_actual}')

    return render(request,"momentos/Carrito.html")

def eliminar_todos_productos(request):
    username_actual = request.session.get('sesionUsuario', 'NoAplica')

    if username_actual != 'NoAplica':
        try:
            usuario_actual = User.objects.get(username=username_actual)
            try:
                carrito_creado = carrito_usuario.objects.get(id_usuario=usuario_actual, esta_completado=False)
                try:
                    carrito_actual = carrito_producto.objects.filter(id_compra=carrito_creado, esta_completado=False).delete()
                except carrito_usuario.DoesNotExist:
                    print(f'El carrito con los productos no existe= {carrito_creado.id_compra}')

            except carrito_usuario.DoesNotExist:
                print(f'El cliente aun no tiene carrito= {usuario_actual.username}')
        except User.DoesNotExist:
            print(f'El cliente no existe con el username= {username_actual}')

    return redirect("momentos:carrito_usuario")

def busqueda_form(request):
    username_actual = request.session.get('sesionUsuario', 'NoAplica')

    if username_actual is not None:
        try:
            usuario_actual = User.objects.get(username=username_actual)
        except User.DoesNotExist:
            print(f'El cliente no existe con el username= {username_actual}')

    paramId_pro = request.GET.get('id')

    if paramId_pro is not None and usuario_actual is not None :
        try:
            carrito_creado = carrito_usuario.objects.get(id_usuario=usuario_actual.id)
            if carrito_creado is None:
                carrito = carrito_usuario(
                    id_usuario = usuario_actual
                )
                carrito.save()
        except carrito_usuario.DoesNotExist:
            print(f'el carrito no existe con el id= {usuario_actual.id}')
            carrito = carrito_usuario(
                id_usuario = usuario_actual
            )
            carrito.save()
    
    return render(request, 'momentos/ResultadoBusqueda.html')

def informacionProducto_form(request):
    return render(request, 'momentos/InformacionProducto.html')