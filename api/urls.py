from django import urls
from rest_framework import urlpatterns
from django.conf.urls import url
from .views import AlumnoBuscarViewSet, AlumnoViewCreateSet, AlumnoViewSet, PersonasViewSet, PersonaBuscarViewSet, PersonaViewCreateSet, CursosViewSet, CursosBuscarViewSet, CursosViewCreateSet, AsistenciaViewSet, AsistenciaBuscarViewSet, AsistenciaViewCreateSet, ProfesorBuscarViewSet, ProfesorViewCreateSet, ProfesorViewSet
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns =[
    url(r'^api/persona/$',PersonasViewSet.as_view()),  
    url(r'^api/buscar_persona/(?P<rut>.+)/$',PersonaBuscarViewSet.as_view()),
    url(r'^api/crear_persona/$',PersonaViewCreateSet.as_view()),  
    url(r'^api/cursos/$',CursosViewSet.as_view()), 
    url(r'^api/buscar_cursos/(?P<id>.+)/$',CursosBuscarViewSet.as_view()), 
    url(r'^api/crear_cursos/$',CursosViewCreateSet.as_view()),
    url(r'^api/asistencia/$',AsistenciaViewSet.as_view()), 
    url(r'^api/buscar_asistencia/(?P<id>.+)/$',AsistenciaBuscarViewSet.as_view()), 
    url(r'^api/crear_asistencia/$',AsistenciaViewCreateSet.as_view()), 
    url(r'^api/profesor/$',ProfesorViewSet.as_view()), 
    url(r'^api/buscar_profesor/(?P<rut>.+)/$',ProfesorBuscarViewSet.as_view()), 
    url(r'^api/crear_profesor/$',ProfesorViewCreateSet.as_view()), 
    url(r'^api/alumno/$',AlumnoViewSet.as_view()), 
    url(r'^api/buscar_alumno/(?P<rut>.+)/$',AlumnoBuscarViewSet.as_view()), 
    url(r'^api/crear_alumno/$',AlumnoViewCreateSet.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)