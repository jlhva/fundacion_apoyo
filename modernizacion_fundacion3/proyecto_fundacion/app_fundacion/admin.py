from django.contrib import admin
from app_fundacion.models import Paciente, Insumos, Aportadores
# Register your models here.
admin.site.register (Paciente)
admin.site.register (Insumos)
admin.site.register (Aportadores)
