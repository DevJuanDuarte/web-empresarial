from operator import mod
from tabnanny import verbose
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Titulo")
    subtitle = models.CharField(max_length=200, verbose_name= "Subtitulo")
    content = models.TextField(verbose_name = "Contenido")
    image = models.ImageField(verbose_name= "Imagen", upload_to = "services")
    published = models.DateTimeField(default = now , verbose_name = "Fecha de publicacion")
    created = models.DateTimeField(auto_now_add = True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Fecha de edicion")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title