# Generated by Django 4.2.7 on 2023-12-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('momentos', '0003_carrito_usuario_historial_usuario_carrito_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito_producto',
            name='esta_completado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='carrito_producto',
            name='total_precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='carrito_usuario',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='historial_usuario',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
