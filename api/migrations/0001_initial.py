# Generated by Django 3.2.9 on 2021-12-06 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('rut', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('rut', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('edad', models.IntegerField()),
                ('tipo', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('rut', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=45)),
                ('fecha', models.DateField()),
                ('rutProfesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('horario', models.DateField()),
                ('idCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cursos')),
                ('rutAlumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.alumno')),
                ('rutProfesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profesor')),
            ],
        ),
    ]
