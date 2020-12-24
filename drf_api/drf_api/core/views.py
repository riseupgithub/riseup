from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import PostSerializer,Post_Doctor,Post_FC,Post_MQ,Post_BG
from .models import *#Paciente,Doctor
from django.template import Template,Context
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login


class TestView(APIView):
    def get(self, request, *args,**kwargs):
        qs=Doctor.objects.all()
        serializer=PostSerializer(qs, many =True)
        return Response(serializer.data)#Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer= PostSerializer(data=request.data)
        if serializer.is_valid():
            if(Paciente.objects.filter(dni=serializer.data["dni"]).exists()):
                return Response(serializer.data,status=201)#Response(serializer.data)
            else: 
                serializer.save()
                return Response(serializer.data,status=201)#Response(serializer.data)
        return Response(serializer.errors,status=404)
class sensado(APIView):
    def get(self, request, *args,**kwargs):
        qs=Doctor.objects.all()
        serializer=Post_Doctor(qs, many =True)
        return Response(serializer.data)#Response(serializer.data)

    def post(self, request, *args,**kwargs):
        paci=PostSerializer(data=request.data)
        if(paci.is_valid() and  Paciente.objects.filter(dni=paci.data["dni"]).exists()):
            qs=Parmetros_directos_sensados.objects.filter(Paciente__dni=paci.data["dni"])#(Paciente=1)#paci.data["id"])
            serializer=Post_FC(qs,many=True)#PostSerializer(qs,many=True)
            return Response(serializer.data)
        else:
            return Response(status=404)
class sen_Mor(APIView):
    def get(self, request, *args,**kwargs):
        qs=Paciente.objects.all()
        serializer=PostSerializer(qs, many =True)
        return Response(serializer.data)#Response(serializer.data)
########################################################################
    def post(self, request, *args,**kwargs):
        paci=PostSerializer(data=request.data)
        if(paci.is_valid() and  Paciente.objects.filter(dni=paci.data["dni"]).exists()):
            qs=Parametros_Morisky.objects.filter(Paciente__dni=paci.data["dni"])#(Paciente=1)#paci.data["id"])
            serializer=Post_MQ(qs,many=True)#PostSerializer(qs,many=True)
            return Response(serializer.data)
        else:
            return Response(status=404)
class sen_BG(APIView):
    def get(self,request,*args,**kwargs):
        qs=Paciente.objects.all()
        serializer=PostSerializer(qs, many =True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        paci=PostSerializer(data=request.data)
        if(paci.is_valid() and  Paciente.objects.filter(dni=paci.data["dni"]).exists()):
            qs=Parametros_Morisky.objects.filter(Paciente__dni=paci.data["dni"])#(Paciente=1)#paci.data["id"])
            serializer=Post_BG(qs,many=True)#PostSerializer(qs,many=True)
            return Response(serializer.data)
        else:
            return Response(status=404)  
#Frontent para el médico  
def prueba(request):#primera vista
    qs=Paciente.objects.values_list("nombre")
    serializer=PostSerializer(qs, many =True)
    m=Doctor.objects.get(dni=72945473).paciente_set.all()
    l=Doctor.objects.get(dni=72945473).num_usuarios()
    return render(request, 'bases/rise.html' ,{'name':m,'perro':l})

def logueo(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        doc= Doctor.objects.values_list("contraseña")
        dac=Doctor.objects.values_list("dni")
        user= authenticate(request, username=username, password=password)
        for i in dac :
            for n in i:
                if (str(n) == username):
                    valordac='t'
                else :
                    valordac="f" 
        for i in doc :
            for n in i:
                if (n == password):
                    valorcon="t"
                else:
                    valorcon="f" 
        if (valorcon=="t" and valordac=="t"):
            return redirect('rise')
                
        
                        
        return render(request,'loguear/log.html',{'error': 'usuario o password inválidos'})
    return render(request, 'loguear/log.html')

def paciente(request):
    lista = []
    qs=Paciente.objects.values_list("nombre")
    m=Doctor.objects.get(dni=72945473).paciente_set.all()
    return render(request, 'paciente/paciente.html' ,{'name':m})