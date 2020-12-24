from django.contrib import admin

from .models import *#Paciente,Doctor

admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Parmetros_directos_sensados)
admin.site.register(Parametros_Borg)
admin.site.register(Parametros_Morisky)