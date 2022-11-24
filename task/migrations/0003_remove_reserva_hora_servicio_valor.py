# Generated by Django 4.1.3 on 2022-11-22 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_remove_servicio_valor_reserva_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='hora',
        ),
        migrations.AddField(
            model_name='servicio',
            name='valor',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
