from django.contrib import admin
from .models import Departamento,Empleado,Cargo,Asistencia,Contrato
# Register your models here.

admin.site.register(Departamento)
admin.site.register(Empleado)
admin.site.register(Cargo)
admin.site.register(Asistencia)
admin.site.register(Contrato)

