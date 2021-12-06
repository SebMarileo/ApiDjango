from django.db.models import fields
from .models import Persona, Cursos, Asistencia, Profesor, Alumno
from rest_framework import serializers

class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ["rut","nombre","apellido","edad","tipo"]

class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = ["id","nombre","horario","fecha","rutProfesor"]

class AsistenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ["id","idCurso","rutAlumno","rutProfesor","fecha","horario"]

class ProfesorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ["rut","nombre","apellido","password"]

class AlumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ["rut","nombre","apellido","password"]