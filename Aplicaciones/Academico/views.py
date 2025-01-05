from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.db import transaction
from .models import Invitacion, Encuesta, Estudiante, Pregunta, Respuesta
# Create your views here.
from .models import Encuesta
from .models import Estudiante
from .models import Invitacion
from .models import Pregunta
from .models import Respuesta
# Create your views here.
#Funcion para presentar en pantalla (renderizar) el codigo html del template inicio.html
def inicio(request):
    return render(request,'inicio.html')

#ENCUESTA
#Presentando en pantalla el formulario de nuevo Encuesta
def nuevaEncuesta(request):
    return render(request,'nuevaEncuesta.html')

#Presentando en pantalla el listado de Encuestas
def listadoEncuesta(request):
    encuestasBdd=Encuesta.objects.all()
    return render(request,'listadoEncuesta.html',{'encuestas':encuestasBdd})

#ESTUDIANTE
#Presentando en pantalla el formulario de nuevo Encuesta
def nuevoEstudiante(request):
    return render(request,'nuevoEstudiante.html')

#Presentando en pantalla el listado de Encuestas
def listadoEstudiante(request):
    estudiantesBdd=Estudiante.objects.all()
    return render(request,'listadoEstudiante.html',{'estudiantes':estudiantesBdd})

#INVITACION
#Presentando en pantalla el formulario de nueva Invitacion 
def nuevaInvitacion(request):
    return render(request,'nuevaInvitacion.html')

#Presentando en pantalla el listado de Encuestas
def listadoInvitacion(request):
    invitacionesBdd=Invitacion.objects.all()
    return render(request,'listadoInvitacion.html',{'invitaciones':invitacionesBdd})

#INVITACION
#Presentando en pantalla el formulario de nueva Invitacion 
def nuevaInvitacion(request):
    encuestas = Encuesta.objects.all()  # Obtiene todas las encuestas
    estudiantes = Estudiante.objects.all()  # Obtiene todos los estudiantes
    return render(request, 'nuevaInvitacion.html', {'encuestas': encuestas, 'estudiantes': estudiantes})

#Presentando en pantalla el listado de Encuestas
def listadoInvitacion(request):
    invitaciones = Invitacion.objects.select_related('encuesta', 'estudiante').all()  # Optimización con select_related
    return render(request, 'listadoInvitacion.html', {'invitaciones': invitaciones})

#PREGUNTA
#Presentando en pantalla el formulario de nueva Invitacion 
def nuevaPregunta(request):
    encuestas = Encuesta.objects.all()  # Cargar encuestas para el select
    return render(request, 'nuevaPregunta.html', {'encuestas': encuestas})

#Presentando en pantalla el listado de Encuestas
def listadoPregunta(request):
    preguntas = Pregunta.objects.select_related('encuesta').all()  # Optimización con select_related
    return render(request, 'listadoPregunta.html', {'preguntas': preguntas})


#RESPUESTA
#Presentando en pantalla el formulario de nueva Invitacion 
def nuevaRespuesta(request):
    estudiantes = Estudiante.objects.all()  # Obtiene todos los estudiantes
    preguntas = Pregunta.objects.all()  # Obtiene todas las preguntas
    return render(request, 'nuevaRespuesta.html', {'estudiantes': estudiantes, 'preguntas': preguntas})


#Presentando en pantalla el listado de Encuestas
def listadoRespuesta(request):
    respuestas = Respuesta.objects.select_related('estudiante', 'pregunta').all()  # Optimización con select_related
    return render(request, 'listadoRespuesta.html', {'respuestas': respuestas})



#GUARDAR ENCUESTA
def guardarEncuesta(request):
    titulo = request.POST['txt_titulo']
    descripcion = request.POST['txt_descripcion']
    fecha_creacion = request.POST['txt_fecha_creacion']
    fecha_expiracion = request.POST['txt_fecha_expiracion']
    estado = request.POST['txt_estado']
    nuevaEncuesta = Encuesta.objects.create(
        titulo=titulo,
        descripcion=descripcion,
        fecha_creacion=fecha_creacion,
        fecha_expiracion=fecha_expiracion,
        estado=estado
    )
    messages.success(request, "Encuesta Insertada")
    return redirect('/listadoEncuesta')

#ELIMINAR ENCUESTA
def eliminarEncuesta(request, id):
    encuestaEliminar = Encuesta.objects.get(id=id)
    encuestaEliminar.delete()
    messages.success(request, "Encuesta Eliminada")
    return redirect('/listadoEncuesta')

def editarEncuesta(request, id):
    encuestaEditar = Encuesta.objects.get(id=id)
    return render(request, "editarEncuesta.html", {'encuesta': encuestaEditar})

def procesarEdicionEncuesta(request):
    encuesta = Encuesta.objects.get(id=request.POST['id'])
    titulo = request.POST['txt_titulo']
    descripcion = request.POST['txt_descripcion']
    fecha_creacion = request.POST['txt_fecha_creacion']
    fecha_expiracion = request.POST['txt_fecha_expiracion']
    estado = request.POST['txt_estado']
    encuesta.titulo = titulo
    encuesta.descripcion = descripcion
    encuesta.fecha_creacion = fecha_creacion
    encuesta.fecha_expiracion = fecha_expiracion
    encuesta.estado = estado
    encuesta.save()
    messages.success(request, "Encuesta Editada Exitosamente")
    return redirect('/listadoEncuesta')


#GUARDAR ESTUDIANTE
def guardarEstudiante(request):
    nombre = request.POST['txt_nombre']
    correo = request.POST['txt_correo']
    matricula = request.POST['txt_matricula']
    fecha_registro = request.POST['txt_fecha_registro']
    nuevoEstudiante = Estudiante.objects.create(
        nombre=nombre,
        correo=correo,
        matricula=matricula,
        fecha_registro=fecha_registro
    )
    messages.success(request, "Estudiante Insertado")
    return redirect('/listadoEstudiante')

#ELIMINAR ESTUDIANTE
def eliminarEstudiante(request, id):
    estudianteEliminar = Estudiante.objects.get(id=id)
    estudianteEliminar.delete()
    messages.success(request, "Estudiante Eliminado")
    return redirect('/listadoEstudiante')

def editarEstudiante(request, id):
    estudianteEditar = Estudiante.objects.get(id=id)
    return render(request, "editarEstudiante.html", {'estudiante': estudianteEditar})

def procesarEdicionEstudiante(request):
    estudiante = Estudiante.objects.get(id=request.POST['id'])
    nombre = request.POST['txt_nombre']
    correo = request.POST['txt_correo']
    matricula = request.POST['txt_matricula']
    fecha_registro = request.POST['txt_fecha_registro'] 
    estudiante.nombre = nombre
    estudiante.correo = correo
    estudiante.matricula = matricula
    estudiante.fecha_registro = fecha_registro
    estudiante.save()
    messages.success(request, "Estudiante Editado Exitosamente")
    return redirect('/listadoEstudiante')


#GUARDAR INVITACION 
def guardarInvitacion(request):
    if request.method == 'POST':
        try:
            # Intenta obtener la encuesta y el estudiante seleccionados
            encuesta = Encuesta.objects.get(id=request.POST['select_encuesta'])
            estudiante = Estudiante.objects.get(id=request.POST['select_estudiante'])
        except Encuesta.DoesNotExist:
            # Si la encuesta no se encuentra, redirige con un mensaje de error
            messages.error(request, "La encuesta seleccionada no existe.")
            return redirect('/nuevaInvitacion/')
        except Estudiante.DoesNotExist:
            # Si el estudiante no se encuentra, redirige con un mensaje de error
            messages.error(request, "El estudiante seleccionado no existe.")
            return redirect('/nuevaInvitacion/')

        # Si la encuesta y el estudiante existen, crea la invitación
        Invitacion.objects.create(
            encuesta=encuesta,
            estudiante=estudiante,
            fecha_envio=datetime.strptime(request.POST['txt_fecha_envio'], '%Y-%m-%d').date(),
            estado=request.POST['txt_estado']
        )

        messages.success(request, "Invitación guardada correctamente.")
        return redirect('/listadoInvitacion/')

    # Si no es POST, redirige al formulario de nueva invitación
    return redirect('/nuevaInvitacion/')

#ELIMINAR INVITACION
def eliminarInvitacion(request, id):
    try:
        with transaction.atomic():
            invitacionEliminar = Invitacion.objects.get(id=id)
            
            # Obtén los IDs relacionados antes de eliminar la invitación
            encuesta_id = invitacionEliminar.encuesta.id
            estudiante_id = invitacionEliminar.estudiante.id
            
            # Elimina la invitación
            invitacionEliminar.delete()
            
            # Elimina registros relacionados si no hay otras invitaciones asociadas
            if not Invitacion.objects.filter(encuesta_id=encuesta_id).exists():
                Encuesta.objects.filter(id=encuesta_id).delete()

            if not Invitacion.objects.filter(estudiante_id=estudiante_id).exists():
                Estudiante.objects.filter(id=estudiante_id).delete()

            messages.success(request, "Invitación y elementos relacionados eliminados.")
    except Invitacion.DoesNotExist:
        messages.error(request, "La invitación no existe.")
    except Exception as e:
        messages.error(request, f"Error al eliminar: {e}")
    
    return redirect('/listadoInvitacion/')

def editarInvitacion(request, id):
    invitacion = get_object_or_404(Invitacion, id=id)
    encuestas = Encuesta.objects.all()
    estudiantes = Estudiante.objects.all()
    
    return render(request, "editarInvitacion.html", {
        'invitacion': invitacion,
        'encuestas': encuestas,
        'estudiantes': estudiantes
    })


def procesarEdicionInvitacion(request):
    if request.method == 'POST':
        try:
            invitacion = Invitacion.objects.get(id=request.POST['id'])
            
            # Actualiza los campos de la invitación
            invitacion.encuesta = Encuesta.objects.get(id=request.POST['select_encuesta'])
            invitacion.estudiante = Estudiante.objects.get(id=request.POST['select_estudiante'])
            invitacion.fecha_envio = datetime.strptime(
                request.POST['txt_fecha_envio'], '%Y-%m-%d'
            ).date()
            invitacion.estado = request.POST['txt_estado']
            
            # Guarda los cambios
            invitacion.save()

            messages.success(request, "Invitación actualizada correctamente.")
        except Invitacion.DoesNotExist:
            messages.error(request, "La invitación no existe.")
        except Encuesta.DoesNotExist:
            messages.error(request, "La encuesta seleccionada no existe.")
        except Estudiante.DoesNotExist:
            messages.error(request, "El estudiante seleccionado no existe.")
        except Exception as e:
            messages.error(request, f"Error al actualizar: {e}")

    return redirect('/listadoInvitacion/')

#GUARDAR PREGUNTA
def guardarPregunta(request):
    if request.method == 'POST':
        try:
            encuesta = Encuesta.objects.get(id=request.POST['select_encuesta'])
        except Encuesta.DoesNotExist:
            messages.error(request, "La encuesta seleccionada no existe.")
            return redirect('/nuevaPregunta/')

        # Cambiar de select_tipo a txt_tipo
        tipo_pregunta = request.POST.get('txt_tipo', None)
        if not tipo_pregunta:
            messages.error(request, "El tipo de pregunta es obligatorio.")
            return redirect('/nuevaPregunta/')

        Pregunta.objects.create(
            texto=request.POST['txt_texto'],
            tipo=tipo_pregunta,
            encuesta=encuesta,
            fecha_crea=datetime.strptime(request.POST['txt_fecha_crea'], '%Y-%m-%d').date()
        )

        messages.success(request, "Pregunta guardada correctamente.")
        return redirect('/listadoPregunta/')

    return redirect('/nuevaPregunta/')

#ELIMINAR PREGUNTA
def eliminarPregunta(request, id):
    try:
        with transaction.atomic():
            preguntaEliminar = Pregunta.objects.get(id=id)
            
            # Obtén los IDs relacionados antes de eliminar la pregunta
            encuesta_id = preguntaEliminar.encuesta.id
            
            # Elimina la pregunta
            preguntaEliminar.delete()
            
            # Elimina registros relacionados si no hay otras preguntas asociadas
            if not Pregunta.objects.filter(encuesta_id=encuesta_id).exists():
                Encuesta.objects.filter(id=encuesta_id).delete()

            messages.success(request, "Pregunta y elementos relacionados eliminados.")
    except Pregunta.DoesNotExist:
        messages.error(request, "La pregunta no existe.")
    except Exception as e:
        messages.error(request, f"Error al eliminar: {e}")
    
    return redirect('/listadoPregunta/')

def editarPregunta(request, id):
    # Obtén la pregunta a editar utilizando get_object_or_404 para asegurar que existe
    pregunta = get_object_or_404(Pregunta, id=id)
    
    # Obtén todas las encuestas disponibles
    encuestas = Encuesta.objects.all()

    return render(request, "editarPregunta.html", {
        'pregunta': pregunta,
        'encuestas': encuestas
    })

def procesarEdicionPregunta(request):
    if request.method == 'POST':
        try:
            pregunta = Pregunta.objects.get(id=request.POST['id'])
            
            # Actualiza los campos de la pregunta
            pregunta.texto = request.POST['txt_texto']
            pregunta.tipo = request.POST['txt_tipo']
            pregunta.encuesta = Encuesta.objects.get(id=request.POST['select_encuesta'])
            pregunta.fecha_crea = datetime.strptime(
                request.POST['txt_fecha_crea'], '%Y-%m-%d'
            ).date()
            
            # Guarda los cambios
            pregunta.save()

            messages.success(request, "Pregunta actualizada correctamente.")
        except Pregunta.DoesNotExist:
            messages.error(request, "La pregunta no existe.")
        except Encuesta.DoesNotExist:
            messages.error(request, "La encuesta seleccionada no existe.")
        except Exception as e:
            messages.error(request, f"Error al actualizar: {e}")

    return redirect('/listadoPregunta/')

#GUARDAR RESPUESTA
def guardarRespuesta(request):
    if request.method == 'POST':
        try:
            # Intenta obtener el estudiante y la pregunta seleccionados
            estudiante = Estudiante.objects.get(id=request.POST['select_estudiante'])
            pregunta = Pregunta.objects.get(id=request.POST['select_pregunta'])
        except Estudiante.DoesNotExist:
            # Si el estudiante no se encuentra, redirige con un mensaje de error
            messages.error(request, "El estudiante seleccionado no existe.")
            return redirect('/nuevaRespuesta/')
        except Pregunta.DoesNotExist:
            # Si la pregunta no se encuentra, redirige con un mensaje de error
            messages.error(request, "La pregunta seleccionada no existe.")
            return redirect('/nuevaRespuesta/')

        # Si el estudiante y la pregunta existen, crea la nueva respuesta
        Respuesta.objects.create(
            estudiante=estudiante,
            pregunta=pregunta,
            texto_respuesta=request.POST['txt_texto_respuesta'],
            fecha_respuesta=datetime.strptime(request.POST['txt_fecha_respuesta'], '%Y-%m-%d').date()
        )

        messages.success(request, "Respuesta guardada correctamente.")
        return redirect('/listadoRespuesta/')

    # Si no es POST, redirige al formulario de nueva respuesta
    return redirect('/nuevaRespuesta/')

#ELIMMINAR RESPUESTA
def eliminarRespuesta(request, id):
    try:
        with transaction.atomic():
            respuestaEliminar = Respuesta.objects.get(id=id)
            
            # Obtén los IDs relacionados antes de eliminar la respuesta
            estudiante_id = respuestaEliminar.estudiante.id
            pregunta_id = respuestaEliminar.pregunta.id
            
            # Elimina la respuesta
            respuestaEliminar.delete()
            
            # Elimina registros relacionados si no hay otras respuestas asociadas
            if not Respuesta.objects.filter(estudiante_id=estudiante_id).exists():
                Estudiante.objects.filter(id=estudiante_id).delete()

            if not Respuesta.objects.filter(pregunta_id=pregunta_id).exists():
                Pregunta.objects.filter(id=pregunta_id).delete()

            messages.success(request, "Respuesta y elementos relacionados eliminados.")
    except Respuesta.DoesNotExist:
        messages.error(request, "La respuesta no existe.")
    except Exception as e:
        messages.error(request, f"Error al eliminar: {e}")
    
    return redirect('/listadoRespuesta/')


def editarRespuesta(request, id):
    # Obtén la respuesta a editar utilizando get_object_or_404 para asegurar que existe
    respuesta = get_object_or_404(Respuesta, id=id)
    
    # Obtén todas las preguntas y estudiantes disponibles
    preguntas = Pregunta.objects.all()
    estudiantes = Estudiante.objects.all()

    return render(request, "editarRespuesta.html", {
        'respuesta': respuesta,
        'preguntas': preguntas,
        'estudiantes': estudiantes
    })

def procesarEdicionRespuesta(request):
    if request.method == 'POST':
        try:
            respuesta = Respuesta.objects.get(id=request.POST['id'])
            
            # Actualiza los campos de la respuesta
            respuesta.texto_respuesta = request.POST['txt_texto_respuesta']
            respuesta.estudiante = Estudiante.objects.get(id=request.POST['select_estudiante'])
            respuesta.pregunta = Pregunta.objects.get(id=request.POST['select_pregunta'])
            respuesta.fecha_respuesta = datetime.strptime(
                request.POST['txt_fecha_respuesta'], '%Y-%m-%d'
            ).date()
            
            # Guarda los cambios
            respuesta.save()

            messages.success(request, "Respuesta actualizada correctamente.")
        except Respuesta.DoesNotExist:
            messages.error(request, "La respuesta no existe.")
        except Estudiante.DoesNotExist:
            messages.error(request, "El estudiante seleccionado no existe.")
        except Pregunta.DoesNotExist:
            messages.error(request, "La pregunta seleccionada no existe.")
        except Exception as e:
            messages.error(request, f"Error al actualizar: {e}")

    return redirect('/listadoRespuesta/')