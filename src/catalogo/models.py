from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings


# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombres, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo!')

        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            nombres=nombres
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, email, nombres, password):
        usuario = self.create_user(
            email,
            username=username,
            nombres=nombres,
            password=password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    nombres = models.CharField('Nombres', max_length=200, blank=True, null=True)
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electronico', max_length=254, unique=True)
    imagen = models.ImageField('Imagen de perfil', upload_to='usuarios', max_length=200, blank=True, null=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombres', 'email']

    def __str__(self):
        return "{}".format(self.nombres)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador


class Clasificacion(models.Model):
    nombre = models.CharField('Nombre', max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = 'Clasificación'
        verbose_name_plural = 'Clasificaciónes'


class Herramientas(models.Model):
    nombre = models.CharField('Nombre', max_length=200, blank=True, null=True)
    imagen = models.ImageField('Imagen', upload_to='herramientas', max_length=200, blank=True, null=True)
    clasificacion = models.ForeignKey(Clasificacion, blank=True, null=True, on_delete=models.CASCADE)
    archivo = models.FileField('Archivo', upload_to='archivos', blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.clasificacion}"

    class Meta:
        verbose_name = 'Herramienta'
        verbose_name_plural = 'Herramientas'

# MODELOS PARA LOS CURSOS
class Videos(models.Model):
    nombre = models.CharField("Nombre", max_length=50, blank=False, null=True)
    url = models.URLField("Link del video", max_length=200, blank=False, null=True)
    curso = models.ForeignKey("Cursos", on_delete=models.CASCADE)
    unidad = models.ForeignKey("Unidades", on_delete=models.CASCADE)
    imagen = models.ImageField("Imagen", upload_to='videos/imagenes', blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.curso}(Unidad-{self.unidad})"
    
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
    
class Unidades(models.Model):
    nombre = models.CharField("Nombre de la unidad", max_length=50, blank=False, null=False)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'

class Cursos(models.Model):
    nombre = models.CharField("Nombre", max_length=50, blank=False, null=False)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'