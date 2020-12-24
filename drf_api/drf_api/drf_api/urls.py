
from django.contrib import admin
from django.urls import path, include
from core.views import *#TestView,sensado
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', TestView.as_view(),name='test'),
    path('sensado/',sensado.as_view(),name="sensado"),
    path('sensadoMQ/',sen_Mor.as_view(),name="sensadoMQ"),
    path('sensadoBG/',sen_BG.as_view(),name="sensadoBG"),
    path('prueba/',prueba, name='rise' ),
    path('loguin/',logueo ,name='login'),
    path('paciente/',paciente,name='paciente'),
]
