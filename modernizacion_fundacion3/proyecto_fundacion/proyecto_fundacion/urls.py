"""proyecto_fundacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app_fundacion import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro_web/',views.registro_web),
    path('registro/',views.registro),
    path('listar_paciente_web/',views.lista_paciente_web),
    path('listar_paciente/',views.listar_paciente),
    path('insumos_web/',views.insumos_web),
    path('ingresar_insumos/',views.ingresar_insumos),
    path('listar_insumos/',views.listar_insumos),
    path('listar_insumos_web/',views.listar_insumos_web),
    path('registrar_aportadores/',views.registrar_aportador),
    path('registrar_aportadores_web/',views.registrar_aportadores_web),
    path('listar_aportadores_web/',views.listar_aportadores_web),
    path('listar_aportadores/',views.listar_aportadores),
    path('pacientes_web/',views.pacientes_web),
    path('entrar_insumos_web/',views.entrar_insumos),
    path('entrar_aportadores_web/',views.entrar_aportadores),
    path('index/',views.index_web),


]
urlpatterns += staticfiles_urlpatterns()