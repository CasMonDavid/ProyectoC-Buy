from django.core.management.base import BaseCommand
from momentos.models import Producto

class Command(BaseCommand):
    help = 'Actualiza la imagen de un producto en la BD Necesita el id para funcionar y se ejecita en el cmd' # py manage.py actualizar_campo_vacio <<ID DEL PRODUCTO>>

    def add_arguments(self, parser):
        parser.add_argument('id_del_registro', type=int, help='ID del registro a actualizar')

    def handle(self, *args, **options):
        id_del_registro = options['id_del_registro']

        try:
            # Buscar el registro por ID
            registro_existente = Producto.objects.get(id=id_del_registro)

            # Verificar si el campo_vacio está vacío
            if not registro_existente.imagen_direccion:
                # Actualizar el campo_vacio con el nuevo valor
                nuevo_valor = 'momentos/imagenes/Computadora (3).png'
                registro_existente.imagen_direccion = nuevo_valor
                registro_existente.save()
                self.stdout.write(self.style.SUCCESS('Registro actualizado con éxito.'))
            else:
                self.stdout.write(self.style.SUCCESS('El campo_vacio no está vacío. No se realizó ninguna actualización.'))
                print(f'Valor de campo_vacio: {registro_existente.imagen_direccion}')
                print(f'Tipo de campo_vacio: {type(registro_existente.imagen_direccion)}')
        except Producto.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'No se encontró ningún registro con ID {id_del_registro}.'))