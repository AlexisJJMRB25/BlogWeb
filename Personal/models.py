from django.db import models

# Create your models here.
class Contacto(models.Model):
    Nombre = models.CharField(max_length=200, blank=True, verbose_name='Nombre')
    Correo = models.EmailField(max_length=200, blank=True, verbose_name='Correo')
    Telefono = models.CharField(max_length=200, blank=True, verbose_name='Telefono')
    Descripcion = models.TextField(null=True)

    def __str__(self):
        return self.Nombre
 

class InformacionPersonal(models.Model):
    Direccion = models.CharField(max_length=200, blank=True, verbose_name='Direccion')
    Telefono1 = models.CharField(max_length=200, blank=True, verbose_name='Telefono1')
    Telefono2 = models.CharField(max_length=200, blank=True, verbose_name='Telefono2')
    Correo1 = models.EmailField(max_length=200, blank=True, verbose_name='Correo1')
    Correo2 = models.EmailField(max_length=200, blank=True, verbose_name='Correo2')


class SobreNosotros(models.Model):
    Imagen = models.ImageField(upload_to = 'sobreNosotros')
    Titulo = models.CharField(max_length=200, blank=True)
    Descripcion = models.CharField(max_length=200, blank=True)