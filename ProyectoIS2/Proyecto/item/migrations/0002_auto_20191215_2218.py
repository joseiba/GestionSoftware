# Generated by Django 2.2.6 on 2019-12-15 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='fecha_modificacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
