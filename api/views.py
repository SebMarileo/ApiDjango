from django.shortcuts import render
from .serializers import AsistenciaSerializers, CursoSerializers, PersonaSerializers, ProfesorSerializers, AlumnoSerializers
from rest_framework import generics
from api.models import Persona, Cursos, Asistencia, Profesor, Alumno
# Create your views here.

# Views Persona
class PersonasViewSet(generics.ListAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializers

class PersonaBuscarViewSet(generics.ListAPIView):
    serializer_class = PersonaSerializers
    def get_queryset(self):
        elrut=self.kwargs["rut"] 
        return Persona.objects.filter(rut=elrut)

class PersonaViewCreateSet(generics.CreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializers

# Views Profesor
class ProfesorViewSet(generics.ListAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializers

class ProfesorBuscarViewSet(generics.ListAPIView):
    serializer_class = ProfesorSerializers
    def get_queryset(self):
        elrut=self.kwargs["rut"] 
        return Profesor.objects.filter(rut=elrut)

class ProfesorViewCreateSet(generics.CreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializers

# Views Alumno
class AlumnoViewSet(generics.ListAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializers

class AlumnoBuscarViewSet(generics.ListAPIView):
    serializer_class = AlumnoSerializers
    def get_queryset(self):
        elrut=self.kwargs["rut"] 
        return Alumno.objects.filter(rut=elrut)

class AlumnoViewCreateSet(generics.CreateAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializers

# Views Cursos
class CursosViewSet(generics.ListAPIView):
    queryset = Cursos.objects.all()
    serializer_class = CursoSerializers

class CursosBuscarViewSet(generics.ListAPIView):
    serializer_class = CursoSerializers
    def get_queryset(self):
        elid=self.kwargs["id"] 
        return Cursos.objects.filter(id=elid)

class CursosViewCreateSet(generics.CreateAPIView):
    queryset = Cursos.objects.all()
    serializer_class = CursoSerializers

# Views Asistencia
class AsistenciaViewSet(generics.ListAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializers

class AsistenciaBuscarViewSet(generics.ListAPIView):
    serializer_class = AsistenciaSerializers
    def get_queryset(self):
        elid=self.kwargs["id"] 
        return Asistencia.objects.filter(id=elid)

class AsistenciaViewCreateSet(generics.CreateAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializers