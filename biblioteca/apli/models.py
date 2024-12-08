from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Carrera(models.Model):
    nombre = models.CharField(max_length=100, default='Sin Nombre')
    descripcion = models.TextField(default='Sin Descripción')

class UsuarioManager(BaseUserManager):
    def create_user(self, nombre, apellido, correo, carrera, password=None, **extra_fields):
        if not correo:
            raise ValueError('El usuario debe tener un correo electrónico')
        correo = self.normalize_email(correo)
        user = self.model(nombre=nombre, apellido=apellido, correo=correo, carrera=carrera, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, apellido, correo, carrera, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(nombre, apellido, correo, carrera, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    puesto = models.CharField(max_length=100, default='Sin Puesto')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'carrera']

    def __str__(self):
        return self.correo

class Autor(models.Model):
    nombre = models.CharField(max_length=100, default='Sin Nombre')
    biografia = models.TextField(default='Sin Biografía')

class Editorial(models.Model):
    nombre = models.CharField(max_length=100, default='Sin Nombre')
    direccion = models.CharField(max_length=255, default='Sin Dirección')
    telefono = models.CharField(max_length=20, default='0000000000')

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, default='Sin Nombre')

class EstadoPrestamo(models.Model):
    nombre = models.CharField(max_length=50, default='Sin Nombre')

class EstadoMulta(models.Model):
    nombre = models.CharField(max_length=50, default='Sin Nombre')

class EstadoLibro(models.Model):
    nombre = models.CharField(max_length=50, default='Sin Estado')

class Libro(models.Model):
    titulo = models.CharField(max_length=200, default='Sin Título')
    descripcion = models.TextField(default='Sin Descripción')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, default=1)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, default=1)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    fecha_publicacion = models.DateField(default='2000-01-01')
    isbn = models.CharField(max_length=13, default='0000000000000')
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, default=1)
    estado = models.ForeignKey(EstadoLibro, on_delete=models.CASCADE, default=1)

class Prestamo(models.Model):
    ESTADO_CHOICES = [
        ('entregado', 'Entregado'),
        ('atrasado', 'Atrasado'),
        ('en_prestamo', 'En Préstamo'),
    ]
    
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, default=1)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    fecha_prestamo = models.DateField(default='2000-01-01')
    fecha_devolucion = models.DateField(default='2000-01-02')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='en_prestamo')

class Multa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    monto = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    fecha = models.DateField(default='2000-01-01')
    estado = models.ForeignKey(EstadoMulta, on_delete=models.CASCADE, default=1)
