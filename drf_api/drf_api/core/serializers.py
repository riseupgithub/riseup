from rest_framework import serializers
from .models import* #Paciente,Doctor
from django import forms



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Paciente
        fields = (
            #aca falta hacer que se visualize 
            #nomas el Identificador
            'id','nombre','apellido','dni','email','contraseña','telefono'
        )
class Post_Doctor(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields = (
            'dni','contraseña'
        )
class Post_FC(serializers.ModelSerializer):
    class Meta:
        model=Parmetros_directos_sensados
        fields=(
            "frecuencia_cardiaca","saturacion_de_oxigeno","Fecha_de_la_medicion","Hora_de_la_medicion"
        )
class Post_MQ(serializers.ModelSerializer):
    class Meta:
        model=Parametros_Morisky
        fields=(
            "pregunta_1","pregunta_2","pregunta_3","pregunta_4","pregunta_5",
            "Fecha_de_la_medicion",
        )
class Post_BG(serializers.ModelSerializer):
    class Meta:
        model=Parametros_Borg
        fields=(
            "puntaje","Fecha_de_la_medicion",
            "Hora_de_la_medicion=models.TimeField()",
        )