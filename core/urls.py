from django.urls import path
from .views import index, entradas

urlpatterns = [
    path('', index, name='index'),
    path('entradas/', entradas, name='entradas')
]