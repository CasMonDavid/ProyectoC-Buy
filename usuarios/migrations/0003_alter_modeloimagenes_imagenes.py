# Generated by Django 4.2.7 on 2023-12-03 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_rename_cbuylogo_modeloimagenes_imagenes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeloimagenes',
            name='imagenes',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
