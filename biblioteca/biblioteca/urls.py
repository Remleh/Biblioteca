"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apli.home.home_view import home_views
from apli.login.login_view import (
    login_views, registro_views, libros_por_carrera, 
    perfil_views, books_view, logout_views,
    cambio_views, solicitar_views, historial_views, book_views)  # Asegúrate de importar book_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views, name='home'),
    path('home/', home_views, name='home'),
    path('login/', login_views, name='login'),
    path('register/', registro_views, name='register'),
    path('profile/', perfil_views, name='perfil'),
    path('carrera/<int:carrera_id>/', libros_por_carrera, name='libros_por_carrera'),
    path('books/', books_view, name='books'), 
    path('books/<int:carrera_id>/', books_view, name='books_by_carrera'),
    path('books/<int:libro_id>/', book_views, name='book'),  # URL para la vista de detalles del libro
    path('logout/', logout_views, name='logout'),
    path('change-password/', cambio_views, name='cambio'),
    path('solicitar/<int:libro_id>/', solicitar_views, name='solicitar'), 
    path('historial/', historial_views, name='historial'),
]
