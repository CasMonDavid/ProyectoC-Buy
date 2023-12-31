# Generated by Django 4.2.7 on 2023-12-06 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('momentos', '0002_producto_imagen_direccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='carrito_usuario',
            fields=[
                ('id_compra', models.AutoField(primary_key=True, serialize=False)),
                ('esta_completado', models.BooleanField(default=False)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='historial_usuario',
            fields=[
                ('id_historial', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('id_compra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='momentos.carrito_usuario')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='carrito_producto',
            fields=[
                ('id_compra_producto', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_pro', models.IntegerField(default=1)),
                ('id_compra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='momentos.carrito_usuario')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='momentos.producto')),
            ],
        ),
    ]
