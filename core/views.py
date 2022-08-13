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

def pesquisa_saidas(request):
    saidas = Saida.objects.all()
    form = PesquisaForm(request.POST or None)
    if str(request.user) != 'AnonymousUser':

        if str(request.method) == 'POST':
            if form.is_valid():
                pesquisa = form.get_categoria()
                cat_pes = int(pesquisa['cat_pes'])
                mes_pes = int(pesquisa['mes_pes'])
                            
                form = PesquisaForm()
                context = {
                    'cat_pes': cat_pes,
                    'mes_pes': mes_pes,
                    'form': form,
                    'saidas': saidas
                }
                return render(request, 'pesquisa_saidas.html', context)
        
        form = PesquisaForm()
        context = {
            'form': form
        }
        return render(request, 'pesquisa_saidas.html', context)
    else:
        return redirect('index')


def pesquisa_entradas(request):
    entradas = Entrada.objects.all()
    form = PesquisaForm(request.POST or None)
    if str(request.user) != 'AnonymousUser':

        if str(request.method) == 'POST':
            if form.is_valid():
                pesquisa = form.get_categoria()
                cat_pes = int(pesquisa['cat_pes'])
                mes_pes = int(pesquisa['mes_pes'])
                            
                form = PesquisaForm()
                context = {
                    'cat_pes': cat_pes,
                    'mes_pes': mes_pes,
                    'form': form,
                    'entradas': entradas
                }
                return render(request, 'pesquisa_entradas.html', context)
        
        form = PesquisaForm()
        context = {
            'form': form
        }
        return render(request, 'pesquisa_entradas.html', context)
    else:
        return redirect('index')