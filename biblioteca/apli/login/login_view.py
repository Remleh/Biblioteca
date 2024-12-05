from django.shortcuts import render

def login_views(request):
    template_name = 'login.html'
    return render (request, template_name)

def registro_views(request):
    template_name = 'registro.html'
    return render (request, template_name)