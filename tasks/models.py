from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.timezone import now
from django.conf import settings

class CustomUserManager(BaseUserManager):
    """
    Manager personalizado para el modelo CustomUser.
    Define métodos para crear usuarios regulares y superusuarios.
    """
    def create_user(self, correo_electronico, nombre_de_usuario, password=None, **extra_fields):
        """
        Crea y guarda un usuario con el correo electrónico y la contraseña.
        """
        if not correo_electronico:
            raise ValueError("El correo electrónico es obligatorio")
        correo_electronico = self.normalize_email(correo_electronico)
        user = self.model(
            correo_electronico=correo_electronico, 
            nombre_de_usuario=nombre_de_usuario, 
            **extra_fields
        )
        user.set_password(password)  # Cifra la contraseña
        user.save(using=self._db)    # Guarda el usuario en la base de datos
        return user

    def create_superuser(self, correo_electronico, nombre_de_usuario, password=None, **extra_fields):
        """
        Crea y guarda un superusuario con permisos de administrador.
        """
        extra_fields.setdefault('es_personal', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('esta_activo', True)

        if extra_fields.get('es_personal') is not True:
            raise ValueError("El superusuario debe tener es_personal=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self.create_user(correo_electronico, nombre_de_usuario, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de usuario personalizado que utiliza el correo electrónico como identificador principal.
    """
    nombre_de_usuario = models.CharField(max_length=150, verbose_name="Nombre de usuario", unique=True)
    correo_electronico = models.EmailField(unique=True, verbose_name="Correo electrónico")
    edad = models.PositiveIntegerField(default=0, verbose_name="Edad")
    es_personal = models.BooleanField(default=False, verbose_name="Es personal")
    esta_activo = models.BooleanField(default=True, verbose_name="Está activo")
    fecha_union = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de unión")

    # Manager personalizado
    objects = CustomUserManager()

    # Definir el campo de identificación principal
    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre_de_usuario']

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        """
        Representación en cadena del usuario (muestra el correo electrónico).
        """
        return self.correo_electronico

    def has_perm(self, perm, obj=None):
        """
        Método requerido por PermissionsMixin
        """
        return self.is_superuser

    def has_module_perms(self, app_label):
        """
        Método requerido por PermissionsMixin
        """
        return self.is_superuser

    @property
    def is_staff(self):
        """
        Propiedad para compatibilidad con el admin de Django
        """
        return self.es_personal

    @property
    def is_active(self):
        """
        Propiedad para compatibilidad con el admin de Django
        """
        return self.esta_activo

class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Usuario"
    )
    title = models.CharField(max_length=255, verbose_name="Título")
    content = models.TextField(blank=True, verbose_name="Descripción")
    completed = models.BooleanField(default=False, verbose_name="Completado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        """
        Representación en cadena de la tarea (muestra el título).
        """
        return self.title

'''from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f'{self.title}, {self.content}'''
