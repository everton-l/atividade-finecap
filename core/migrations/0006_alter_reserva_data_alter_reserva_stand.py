# Generated by Django 4.2.5 on 2023-09-27 13:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_merge_0003_alter_reserva_stand_0004_alter_stand_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='stand',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.stand'),
        ),
    ]