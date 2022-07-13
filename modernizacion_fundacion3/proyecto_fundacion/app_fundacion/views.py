from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app_fundacion.models import Paciente
from app_fundacion.models import Insumos
from app_fundacion.models import Aportadores

def registro_web(request):
    return render(request,"registrar.html")

def registro(request):
    nombre=request.GET["nombre"]
    rut=request.GET["rut"]
    correo=request.GET["correo"]
    hijos=request.GET["hijos"]
    nacionalidad=request.GET["nacionalidad"]
    cuidados=request.GET["cuidados"]
    telefono=request.GET["telefono"]
    estado_civil=request.GET["estado"]
    if len(nombre)>0 and len(rut)>0 and len(correo)>0 and len(hijos)>0 and len(nacionalidad)>0 and len(cuidados)>0 and len(telefono)>0 and len(estado_civil)>0:
        info = Paciente(nombre_completo=nombre, rut=rut, correo=correo, hijos=hijos, nacionalidad=nacionalidad, cuidados_especiales=cuidados, telefono=telefono, estado_civil=estado_civil)
        info.save()
        mensaje="Paciente ingresado"
    else:
        mensaje="Error al ingresar el paciente"
    return HttpResponse(mensaje)

def lista_paciente_web(request):
    return render(request,"listar_paciente.html")

def listar_paciente(request):
    datos = Paciente.objects.all()
    return render(request,"listar_paciente.html",{'informacion':datos})

def insumos_web(request):
    return render(request,"insumos.html")

def ingresar_insumos(request):
    medicamento=request.GET["medicamento"]
    stock=request.GET["stock"]
    laboratorio=request.GET["laboratorio"]
    if len (medicamento) >0 and len (stock) >0 and len (laboratorio)>0:
        info = Insumos(medicamento=medicamento ,stock=stock,laboratorio=laboratorio)
        info.save()
        mensaje="insumo ingresado"
    else:
        mensaje="Error al ingresar el insumo"
    return HttpResponse(mensaje)

def listar_insumos(request):
    datos = Insumos.objects.all()
    return render(request,"listar_insumos.html",{'informacion':datos})

def listar_insumos_web(request):
    return render(request,"listar_insumos.html")

def registrar_aportador(request):
    nombreAportador=request.GET["nombre_aportador"]
    rutAportador=request.GET["rut_aportador"]
    correoAportador=request.GET["correo_aportador"]
    peticion=request.GET["peticion"]
    pais=request.GET["nacionalidad_aportador"]
    monto=request.GET["monto"]
    if len (nombreAportador) >0 and len (rutAportador) >0 and len (correoAportador)>0 and len (peticion)>0 and len (pais)>0 and len (monto)>0 :
        info = Aportadores(nombreAportador=nombreAportador ,rutAportador=rutAportador,correoAportador=correoAportador,peticion=peticion,pais=pais,monto=monto)
        info.save()
        mensaje="aportador ingresado"
    else:
        mensaje="Error al ingresar el aportador"
    return HttpResponse(mensaje)

def registrar_aportadores_web(request):
    return render(request,"registrar_aportadores.html")

def listar_aportadores(request):
    datos = Aportadores.objects.all()
    return render(request,"listar_aportadores.html",{'informacion':datos})

def listar_aportadores_web(request):
    return render(request,"listar_aportadores.html")

def pacientes_web(request):
    return render(request,"pacientes.html")

def entrar_insumos(request):
    return render(request,"entrar_insumos.html")

def entrar_aportadores(request):
    return render(request,"entrar_aportadores.html")

def index_web(request):
    return render(request,"index.html")
