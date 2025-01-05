from django.db import models

# Create your models here.


class Encuesta(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    fecha_creacion=models.DateField()
    fecha_expiracion=models.DateField()
    estado=models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50)
    fecha_registro = models.DateField()

    def __str__(self):
        return self.nombre

class Invitacion(models.Model):
    id = models.AutoField(primary_key=True)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha_envio = models.DateField()
    estado = models.CharField(max_length=20)  # Pendiente/Completada

    def __str__(self):
        return f"{self.encuesta.titulo} {self.estudiante.nombre}"

class Pregunta(models.Model):
    id=models.AutoField(primary_key=True)
    texto=models.CharField(max_length=255)
    tipo=models.CharField(max_length=50)
    encuesta=models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    fecha_crea=models.DateField()

    def __str__(self):
        return self.texto

class Respuesta(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_respuesta = models.CharField(max_length=255)
    fecha_respuesta = models.DateField()

    def __str__(self):
        return f"{self.estudiante.nombre} {self.pregunta.texto}"

