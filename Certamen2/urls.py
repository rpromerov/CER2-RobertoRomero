"""
URL configuration for Certamen2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from Certamen2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="Inicio"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('nuevo_proyecto/', views.agregar_proyecto, name='nuevo_proyecto'),
    path('editar_proyecto/<int:project_id>/', views.agregar_proyecto, name='editar_proyecto'),
    path('eliminar_proyecto/<int:project_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('patrocinar_proyecto/<int:project_id>/', views.patrocinar_proyecto, name='patrocinar_proyecto'),
]
