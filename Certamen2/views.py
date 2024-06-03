from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import *
from .models import *


def home(request):
    title = "Inicio"
    logged_user = request.session.get('user_id', None)

    if logged_user is not None:
        user = Usuario.objects.get(id=logged_user)
        if user.role == '0':
            projects = Proyecto.objects.filter(estudiante=user)
        else:
            projects = Proyecto.objects.all()
    else:
        user = None

        projects = Proyecto.objects.filter(profesor__isnull=False)
    temas = set(p.tema for p in projects)
    data = {
        "title": title,
        "projects": projects,
        "temas": temas,
        "user": user
    }

    return render(request, 'landing.html', data)


def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        try:
            user = Usuario.objects.get(email=email)
            if user.password == password:
                request.session['user_id'] = user.id
                return redirect('/')
            else:
                messages.error(request, 'Contraseña invalida.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no existe.')
    return render(request, 'home.html')


def logout_view(request):
    request.session['user_id'] = None
    return redirect('/')


def agregar_proyecto(request, project_id=None):
    estudiante = request.session.get('user_id', None)
    if estudiante is not None:
        estudiante = Usuario.objects.get(id=estudiante)
    else:
        messages.error(request, 'Debe iniciar sesión para agregar un proyecto.')
        return redirect('/')

    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            if project_id:  # This is an existing project, update it
                project = Proyecto.objects.get(id=project_id)
                form = ProyectoForm(request.POST, instance=project)
            else:  # This is a new project, create it
                form.instance.estudiante = estudiante
            form.save()
            messages.success(request, 'Proyecto guardado correctamente.')
            return redirect('/')
        else:
            messages.error(request, 'Error al guardar el proyecto.')
    else:
        project = Proyecto.objects.get(id=project_id) if project_id is not None else None
        form = ProyectoForm(instance=project)
        return render(request, 'newProject.html', {'form': form, 'project': project})


def eliminar_proyecto(request, project_id):
    if request.method == 'POST':
        proyecto = Proyecto.objects.get(id=project_id)
        proyecto.delete()
        messages.success(request, 'Proyecto eliminado correctamente.')
    return redirect('Inicio')


def patrocinar_proyecto(request, project_id):
    proyecto = Proyecto.objects.get(id=project_id)
    proyecto.profesor = Usuario.objects.get(id=request.session['user_id'])
    proyecto.save()
    messages.success(request, 'Proyecto patrocinado correctamente.')
    return redirect('Inicio')
