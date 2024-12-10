from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from .models import Libro, Autor, Editorial, Categoria, Carrera, EstadoLibro, Prestamo

# Pruebas Unitarias para el Modelo Libro
class LibroModelTest(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(nombre='Juan Pérez', biografia='Autor especializado en algoritmos y programación.')
        self.editorial = Editorial.objects.create(nombre='Editorial Alfa', direccion='123 Calle Principal', telefono='1234567890')
        self.categoria = Categoria.objects.create(nombre='Informática')
        self.carrera = Carrera.objects.create(nombre='ISC', descripcion='Ingeniería en Sistemas Computacionales')
        self.estado = EstadoLibro.objects.create(nombre='Disponible')

    def test_crear_libro(self):
        libro = Libro.objects.create(
            titulo='Algoritmos y Programación',
            descripcion='Libro sobre algoritmos y programación.',
            autor=self.autor,
            editorial=self.editorial,
            categoria=self.categoria,
            fecha_publicacion='2022-01-01',
            isbn='9781234567890',
            carrera=self.carrera,
            estado=self.estado
        )
        self.assertEqual(libro.titulo, 'Algoritmos y Programación')
        self.assertEqual(libro.autor.nombre, 'Juan Pérez')
        self.assertEqual(libro.editorial.nombre, 'Editorial Alfa')
    
    def test_libro_sin_titulo(self):
        with self.assertRaises(IntegrityError):
            Libro.objects.create(
                titulo=None, 
                descripcion='Libro sin título.',
                autor=self.autor,
                editorial=self.editorial,
                categoria=self.categoria,
                fecha_publicacion='2022-01-01',
                isbn='9781234567890',
                carrera=self.carrera,
                estado=self.estado
            )

    def test_actualizar_libro(self):
        libro = Libro.objects.create(
            titulo='Algoritmos y Programación',
            descripcion='Libro sobre algoritmos y programación.',
            autor=self.autor,
            editorial=self.editorial,
            categoria=self.categoria,
            fecha_publicacion='2022-01-01',
            isbn='9781234567890',
            carrera=self.carrera,
            estado=self.estado
        )
        libro.titulo = 'Algoritmos Avanzados'
        libro.save()
        libro_actualizado = Libro.objects.get(id=libro.id)
        self.assertEqual(libro_actualizado.titulo, 'Algoritmos Avanzados')

# Pruebas de Integración para la Creación de Préstamos
class PrestamoIntegrationTest(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(nombre='Juan Pérez', biografia='Autor especializado en algoritmos y programación.')
        self.editorial = Editorial.objects.create(nombre='Editorial Alfa', direccion='123 Calle Principal', telefono='1234567890')
        self.categoria = Categoria.objects.create(nombre='Informática')
        self.carrera = Carrera.objects.create(nombre='ISC', descripcion='Ingeniería en Sistemas Computacionales')
        self.estado = EstadoLibro.objects.create(nombre='Disponible')
        self.libro = Libro.objects.create(
            titulo='Algoritmos y Programación',
            descripcion='Libro sobre algoritmos y programación.',
            autor=self.autor,
            editorial=self.editorial,
            categoria=self.categoria,
            fecha_publicacion='2022-01-01',
            isbn='9781234567890',
            carrera=self.carrera,
            estado=self.estado
        )
        self.user = get_user_model().objects.create_user(
            nombre='Test',
            apellido='User',
            correo='test@example.com',
            carrera=self.carrera,
            password='testpassword123'
        )

    def test_crear_prestamo(self):
        prestamo = Prestamo.objects.create(
            libro=self.libro,
            usuario=self.user,
            fecha_prestamo='2023-01-01',
            fecha_devolucion='2023-02-01',
            estado='en_prestamo'
        )
        self.assertEqual(prestamo.libro.titulo, 'Algoritmos y Programación')
        self.assertEqual(prestamo.usuario.correo, 'test@example.com')
        self.assertEqual(prestamo.estado, 'en_prestamo')
    
    def test_prestamo_sin_usuario(self):
        with self.assertRaises(IntegrityError):
            Prestamo.objects.create(
                libro=self.libro,
                usuario=None,  
                fecha_prestamo='2023-01-01',
                fecha_devolucion='2023-02-01',
                estado='en_prestamo'
            )

    def test_actualizar_estado_prestamo(self):
        prestamo = Prestamo.objects.create(
            libro=self.libro,
            usuario=self.user,
            fecha_prestamo='2023-01-01',
            fecha_devolucion='2023-02-01',
            estado='en_prestamo'
        )
        prestamo.estado = 'entregado'
        prestamo.save()
        prestamo_actualizado = Prestamo.objects.get(id=prestamo.id)
        self.assertEqual(prestamo_actualizado.estado, 'entregado')
