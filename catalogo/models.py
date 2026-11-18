from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=150)

    codigo = models.CharField(max_length=7, unique=True)

    foto = models.ImageField(upload_to="productos/", blank=True, null=True)

    descripcion = models.TextField()

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
