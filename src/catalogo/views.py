import os.path

from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import (
    Herramientas,
    Usuario,
    Videos
)
from .forms import (
    FormLogin,
    FormRegister
)


# Create your views here.

@login_required
def Inicio(request):
    busqueda = request.POST.get("buscar")
    busquedaCurso = request.POST.get("buscarVideo")
    if busqueda:
        herramientas = Herramientas.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(clasificacion__nombre__icontains=busqueda)
        ).distinct()
    elif busquedaCurso:
        videos = Videos.objects.filter(
            Q(nombre__icontains=busquedaCurso)
        )
    else:
        videos = Videos.objects.all()
        herramientas = Herramientas.objects.all()

    data = {
        'Herramientas': herramientas,
        'Videos': videos,
        'Texto': 'Textito'
    }
    return render(request, 'index.html', data)

def vistaLoginRegister(request):
    formRegister = FormRegister()

    data = {
        'formRegister': formRegister,
        'nombre': 'Emilio',
    }
    return render(request, 'registration/login.html', data)

def crear_usuario(request):
    print("Entró a la función CrearUsuario")
    if request.method == 'POST':
        formulario = FormRegister(request.POST, files=request.FILES)
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            nombres = data_form.get('nombres')
            username = data_form.get('username')
            correo = data_form.get('email')
            imagen = data_form.get('imagen')
            password = make_password(data_form.get('password'))

            print(f"Ya se obtuvieron los datos del formulario, el nombre es: {nombres}")

            crearusuario = Usuario(
                nombres=nombres,
                username=username,
                email=correo,
                imagen=imagen,
                password=password,
            )
            crearusuario.save()
            return redirect(to='login')
    else:
        formulario = FormRegister()
    return render(request, 'registration/login.html', {
        'form': formulario
    })

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404
