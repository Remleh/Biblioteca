from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.utils import timezone
from ..models import Libro, Carrera, Usuario, Prestamo
from ..forms import RegistroForm, LoginForm, CustomPasswordChangeForm, SolicitarPrestamoForm

# Vista para la página de registro
def registro_views(request):
    carreras = Carrera.objects.all()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form, 'carreras': carreras})

# Vista para mostrar los libros por carrera
def libros_por_carrera(request, carrera_id):
    carrera = get_object_or_404(Carrera, id=carrera_id)
    libros = Libro.objects.filter(carrera=carrera)
    carreras = Carrera.objects.all()
    return render(request, 'books.html', {'carrera': carrera, 'libros': libros, 'carreras': carreras})

# Vista para el perfil del usuario
@login_required(login_url='/login/')
def perfil_views(request):
    usuario = request.user
    return render(request, 'profile.html', {'usuario': usuario})

# Vista para iniciar sesión
def login_views(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=nombre, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciales incorrectas. Inténtalo de nuevo.')
        else:
            messages.error(request, 'Error al validar el formulario. Inténtalo de nuevo.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Vista para mostrar todos los libros o libros por carrera específica
def books_view(request, carrera_id=None):
    carreras = Carrera.objects.all()
    if carrera_id:
        libros = Libro.objects.filter(carrera_id=carrera_id)
    else:
        libros = Libro.objects.all()
    return render(request, 'books.html', {'libros': libros, 'carreras': carreras})

# Vista para cerrar sesión
def logout_views(request):
    logout(request)
    return redirect('login')

# Vista para cambiar la contraseña del usuario
@login_required(login_url='/login/')
def cambio_views(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu contraseña ha sido actualizada con éxito.')
            return redirect('perfil')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change.html', {'form': form})

# Vista para solicitar un préstamo
@login_required(login_url='/login/')
def solicitar_views(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        form = SolicitarPrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.usuario = request.user
            prestamo.libro = libro
            prestamo.fecha_prestamo = timezone.now()
            prestamo.save()
            messages.success(request, 'El préstamo se ha realizado con éxito.')
            return redirect('historial')
    else:
        form = SolicitarPrestamoForm()
    return render(request, 'solicitar.html', {'libro': libro, 'form': form})

# Vista para mostrar el historial de préstamos del usuario
@login_required(login_url='/login/')
def historial_views(request):
    prestamos = Prestamo.objects.filter(usuario=request.user)
    return render(request, 'historial.html', {'prestamos': prestamos})

# Vista para la página de detalles del libro
def book_views(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    return render(request, 'book.html', {'libro': libro})

# Vista para la página de inicio (home)
def home_views(request):
    carreras = Carrera.objects.all()
    return render(request, 'home.html', {'carreras': carreras})
