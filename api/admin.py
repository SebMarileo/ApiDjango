from django.contrib import admin
from .models import Alumno, Asistencia, Cursos, Persona, Profesor

# Register your models here.
admin.site.register(Persona)
admin.site.register(Cursos)
admin.site.register(Asistencia)
admin.site.register(Profesor)
admin.site.register(Alumno)