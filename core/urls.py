from django.urls import path
from .views import index, entradas, saidas, poupanca
from .views import pesquisa_saidas, pesquisa_entradas

urlpatterns = [
    path('', index, name='index'),
    path('entradas/', entradas, name='entradas'),
    path('saidas/', saidas, name='saidas'),
    path('pesquisa_saidas/', pesquisa_saidas, name='pesquisa_saidas'),
    path('pesquisa_entradas/', pesquisa_entradas, name='pesquisa_entradas'),
    path('pesquisa_entradas/', pesquisa_entradas, name='pesquisa_entradas'),
    path('poupanca/', poupanca, name='poupanca'),
]