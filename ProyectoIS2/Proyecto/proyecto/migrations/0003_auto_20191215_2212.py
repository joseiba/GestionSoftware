# Generated by Django 2.2.6 on 2019-12-15 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0002_proyecto_usu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='estado',
            field=models.CharField(choices=[('ACT', 'Activo'), ('BLO', 'Bloqueado'), ('FIN', 'Finalizado')], default='ACT', max_length=15),
        ),
    ]
