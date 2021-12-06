from django import urls
from rest_framework import urlpatterns
from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns =[
    url(r'^api/persona/$',views.PersonasViewSet.as_view()),  
    url(r'^api/buscar_persona/(?P<rut>.+)/$',views.PersonaBuscarViewSet.as_view()),
    url(r'^api/crear_persona/$',views.PersonaViewCreateSet.as_view()),  
    url(r'^api/cursos/$',views.CursosViewSet.as_view()), 
    url(r'^api/buscar_cursos/(?P<id>.+)/$',views.CursosBuscarViewSet.as_view()), 
    url(r'^api/crear_cursos/$',views.CursosViewCreateSet.as_view()),
    url(r'^api/asistencia/$',views.AsistenciaViewSet.as_view()), 
    url(r'^api/buscar_asistencia/(?P<id>.+)/$',views.AsistenciaBuscarViewSet.as_view()), 
    url(r'^api/crear_asistencia/$',views.AsistenciaViewCreateSet.as_view()), 
    url(r'^api/profesor/$',views.ProfesorAPI), 
    #url(r'^api/buscar_profesor/(?P<rut>.+)/$',views.ProfesorBuscarViewSet.as_view()), 
    #url(r'^api/crear_profesor/$',views.ProfesorViewCreateSet.as_view()), 
    url(r'^api/alumno/$',views.AlumnoViewSet.as_view()), 
    url(r'^api/buscar_alumno/(?P<rut>.+)/$',views.AlumnoBuscarViewSet.as_view()), 
    url(r'^api/crear_alumno/$',views.AlumnoViewCreateSet.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)