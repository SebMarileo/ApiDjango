from django.db import models

# Create your models here.
class Persona(models.Model):
    rut = models.CharField(primary_key=True,max_length=45)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    edad = models.IntegerField()
    tipo = models.IntegerField(default=1)

    def __str__(self):
        return self.rut

class Profesor(models.Model):
    rut = models.CharField(primary_key=True,max_length=45)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    def __str__(self):
        return self.rut

class Alumno(models.Model):
    rut = models.CharField(primary_key=True,max_length=45)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    def __str__(self):
        return self.rut

class Cursos(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=50)
    horario = models.CharField(max_length=45)
    fecha = models.DateField()
    rutProfesor = models.ForeignKey(Profesor,on_delete=models.CASCADE)

    def __str__(self):
        return self.id+' '+self.nombre

class Asistencia(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    idCurso = models.ForeignKey(Cursos,on_delete=models.CASCADE)
    rutAlumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    rutProfesor = models.ForeignKey(Profesor,on_delete=models.CASCADE)
    fecha = models.DateField()
    horario = models.DateField()

    def __str__(self):
        return self.id