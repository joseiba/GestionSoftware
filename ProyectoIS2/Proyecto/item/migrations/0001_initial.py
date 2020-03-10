# Generated by Django 2.2.6 on 2019-12-15 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lineab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField()),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_modificacion', models.DateField(null=True)),
                ('linea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lineab.Linea_Base')),
            ],
        ),
    ]
