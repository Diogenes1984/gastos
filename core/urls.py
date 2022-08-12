from django.urls import path
from .views import index, entradas, saidas, pesquisa

urlpatterns = [
    path('', index, name='index'),
    path('entradas/', entradas, name='entradas'),
    path('saidas/', saidas, name='saidas'),
    path('pesquisa/', pesquisa, name='pesquisa'),
]