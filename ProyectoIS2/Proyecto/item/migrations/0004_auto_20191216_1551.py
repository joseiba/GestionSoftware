# Generated by Django 2.2.6 on 2019-12-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20191216_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='fecha_modificacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
