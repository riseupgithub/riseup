from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator,MaxValueValidator
import datetime
# Create your models here.

User=get_user_model()

class Doctor(models.Model):
    #identificador=models.IntegerField(default=2)
    dni= models.IntegerField(default=10000000,validators=[MinValueValidator(10000000),MaxValueValidator(99999999)],null=False,blank=False,primary_key=True)
    contraseña=models.CharField(max_length=100)# una validaddor seria unos requisitos para seguridad
    #Nusuarios=models.IntegerField(default=0)##########################FAL
    def __str__(self):
        return str(self.dni)

    def num_usuarios(self):
        number=self.paciente_set.all()
        return (len(list(number))) 
#####################################################################################################
class Paciente(models.Model):
    id   = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50,null=True)
    apellido=models.CharField(max_length=50,null=True)
    dni = models.IntegerField(default=10000000,validators=[MinValueValidator(10000000),
        MaxValueValidator(99999999)],null=False,blank=False)
    email = models.EmailField(max_length=100,blank=True)
    contraseña=models.CharField(max_length=100,null=False,blank=False)
    telefono = models.IntegerField(default=100000000,
        validators=[MinValueValidator(100000000),MaxValueValidator(999999999)],
        null=True,blank=True)

    ###########many to one  #### un paciente tiene su doctor  y el  doctor tiene sus n pacientes
    doctor=models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True)
        #,default=None)
    
    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido)+" "+str(self.dni)
#######################################################################################################
class Parmetros_directos_sensados(models.Model):
    #faltal los de inter1relacion
    frecuencia_cardiaca=models.FloatField(blank=True)
    saturacion_de_oxigeno=models.FloatField(blank=True)
    Fecha_de_la_medicion=models.DateField(("Date"), default=datetime.date.today)
    Hora_de_la_medicion=models.TimeField()

    ###########many to one  #### un paciente tiene su doctor  y el  doctor tiene sus n pacientes
    Paciente=models.ForeignKey(Paciente,on_delete=models.CASCADE
        ,default=None,blank=True)
    def __str__(self):
        return str(self.frecuencia_cardiaca)
###########################################################################################################
class Parametros_Morisky(models.Model):
    #faltal los de interrelacion
    pregunta_1=models.BooleanField()
    pregunta_2=models.BooleanField()
    pregunta_3=models.BooleanField()
    pregunta_4=models.BooleanField()
    pregunta_5= models.IntegerField(default=1,validators=[MinValueValidator(1),
         MaxValueValidator(5)])
    Fecha_de_la_medicion=models.DateField(("Date"), default=datetime.date.today)
    ###########many to one  #### un paciente tiene su doctor  y el  doctor tiene sus n pacientes
    Paciente=models.ForeignKey(Paciente,on_delete=models.CASCADE
        ,default=None,blank=True)
    def __str__(self):
        return str(self.pregunta_1)
###############################################################################################################
class Parametros_Borg(models.Model):
    #faltal los de interrelacion
    puntaje=models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(10)])
    Fecha_de_la_medicion=models.DateField(("Date"), default=datetime.date.today)
    Hora_de_la_medicion=models.TimeField()
    ###########many to one  #### un paciente tiene su doctor  y el  doctor tiene sus n pacientes
    Paciente=models.ForeignKey(Paciente,on_delete=models.CASCADE
        ,default=None,blank=True)
    def __str__(self):
        return str(self.puntaje)