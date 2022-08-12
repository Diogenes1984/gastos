from django.shortcuts import render, redirect
from .models import Categoria, Entrada, Saida
from .utils import somaEntradasMeses, somaSaidaMeses
from .forms import PesquisaForm

def index(request):
    context = {
        'logado': True
    }

    if str(request.user) != 'AnonymousUser':

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
        #return redirect('index')



    #return render(request, 'index.html')

def entradas(request):


    context = somaEntradasMeses()

    if str(request.user) != 'AnonymousUser':

        return render(request, 'entradas.html', context)
    else:
        #return render(request, 'entradas.html')
        return redirect('index')

def saidas(request):
    
    context = somaSaidaMeses()
    if str(request.user) != 'AnonymousUser':

        return render(request, 'saidas.html', context)
    else:
        return redirect('index')

def pesquisa(request):
    saidas = Saida.objects.all()
    form = PesquisaForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            pesquisa = int(form.get_categoria())
                        
            form = PesquisaForm()
            context = {
                'pesquisa': pesquisa,
                'form': form,
                'saidas': saidas
            }
            return render(request, 'pesquisa.html', context)
    
    form = PesquisaForm()
    context = {
        'form': form
    }
    return render(request, 'pesquisa.html', context)
    