#URLS especificas de la Aplicacion "Matriculas"
from django.urls import path
from . import views
urlpatterns = [
    # Encuesta
    path('',views.inicio),
    path('nuevaEncuesta/', views.nuevaEncuesta),
    path('listadoEncuesta/', views.listadoEncuesta),
    path('guardarEncuesta/', views.guardarEncuesta),
    path('eliminarEncuesta/<id>', views.eliminarEncuesta),
    path('editarEncuesta/<id>', views.editarEncuesta),
    path('procesarEdicionEncuesta/', views.procesarEdicionEncuesta),

    # Estudiante
    path('nuevoEstudiante/', views.nuevoEstudiante),
    path('listadoEstudiante/', views.listadoEstudiante),
    path('guardarEstudiante/', views.guardarEstudiante),
    path('eliminarEstudiante/<id>', views.eliminarEstudiante),
    path('editarEstudiante/<id>', views.editarEstudiante),
    path('procesarEdicionEstudiante/', views.procesarEdicionEstudiante),
    
    # Invitación
    path('nuevaInvitacion/', views.nuevaInvitacion),
    path('listadoInvitacion/', views.listadoInvitacion),
    path('guardarInvitacion/', views.guardarInvitacion),
    path('eliminarInvitacion/<id>', views.eliminarInvitacion),
    path('editarInvitacion/<id>', views.editarInvitacion),
    path('procesarEdicionInvitacion/', views.procesarEdicionInvitacion),

    # Pregunta
    path('nuevaPregunta/', views.nuevaPregunta),
    path('listadoPregunta/', views.listadoPregunta),
    path('guardarPregunta/', views.guardarPregunta),
    path('eliminarPregunta/<id>', views.eliminarPregunta),
    path('editarPregunta/<id>', views.editarPregunta),
    path('procesarEdicionPregunta/', views.procesarEdicionPregunta),

    # Respuesta
    path('nuevaRespuesta/', views.nuevaRespuesta),
    path('guardarRespuesta/', views.guardarRespuesta),
    path('listadoRespuesta/', views.listadoRespuesta),
    path('eliminarRespuesta/<id>', views.eliminarRespuesta),
    path('editarRespuesta/<id>', views.editarRespuesta),
    path('procesarEdicionRespuesta/', views.procesarEdicionRespuesta),
]
