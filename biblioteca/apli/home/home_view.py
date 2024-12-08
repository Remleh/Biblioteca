from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Carrera

@login_required(login_url='/login/')
def home_views(request):
    carreras = Carrera.objects.all()
    context = {
        'carreras': carreras
    }
    return render(request, 'index.html', context)


