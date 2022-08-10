import datetime
from django.shortcuts import render, redirect
from .models import Categoria, Entrada, Saida


def index(request):
    return render(request, 'index.html')

def entradas(request):

    entradas = Entrada.objects.all()
    


    aux = 0
    for entrada in entradas:
        aux += entrada.valor
    
    context = {
        'entradas': entradas,
        'soma': aux
    }

    if str(request.user) != 'AnonymousUser':

        return render(request, 'entradas.html', context)
    else:
        #return render(request, 'entradas.html')
        return redirect('index')