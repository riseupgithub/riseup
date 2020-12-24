# Generated by Django 3.1.4 on 2020-12-16 05:39

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('dni', models.IntegerField(default=10000000, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)])),
                ('contraseña', models.CharField(max_length=100)),
                ('Nusuarios', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('apellido', models.CharField(max_length=50, null=True)),
                ('dni', models.IntegerField(default=10000000, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)])),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
                ('telefono', models.IntegerField(blank=True, default=100000000, null=True, validators=[django.core.validators.MinValueValidator(100000000), django.core.validators.MaxValueValidator(999999999)])),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Parmetros_directos_sensados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frecuencia_cardiaca', models.FloatField(blank=True)),
                ('saturacion_de_oxigeno', models.FloatField(blank=True)),
                ('Fecha_de_la_medicion', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Hora_de_la_medicion', models.TimeField()),
                ('Paciente', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Parametros_Morisky',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta_1', models.BooleanField()),
                ('pregunta_2', models.BooleanField()),
                ('pregunta_3', models.BooleanField()),
                ('pregunta_4', models.BooleanField()),
                ('pregunta_5', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Fecha_de_la_medicion', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Paciente', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Parametros_Borg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('Fecha_de_la_medicion', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Hora_de_la_medicion', models.TimeField()),
                ('Paciente', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
            ],
        ),
    ]