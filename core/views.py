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

    form = PesquisaForm(request.POST or None)
    if str(request.user) != 'AnonymousUser':

        if str(request.method) == 'POST':
            if form.is_valid():
                pesquisa = form.get_categoria()
                cat_pes = int(pesquisa['cat_pes'])
                mes_pes = int(pesquisa['mes_pes'])
                            
                if (mes_pes == 0 and cat_pes == 0):
                    saidas = Saida.objects.all()
                    soma = 0
                    for saida in saidas:
                        soma += saida.valor

                    form = PesquisaForm()
               
                    context = {
                        'form': form,
                        'saidas': saidas,
                        'soma': soma
                    }
                    return render(request, 'pesquisa_saidas.html', context)
                elif (mes_pes == 0):
                    saidas = Saida.objects.all().filter(categoria__id=cat_pes)
                    soma = 0
                    for saida in saidas:
                        soma += saida.valor

                    form = PesquisaForm()
               
                    context = {
                        'form': form,
                        'saidas': saidas,
                        'soma': soma

                    }
                    return render(request, 'pesquisa_saidas.html', context)
                elif (cat_pes == 0):
                    saidas = Saida.objects.all().filter(data__month=mes_pes)

                    soma = 0
                    for saida in saidas:
                        soma += saida.valor

                    form = PesquisaForm()
               
                    context = {
                        'form': form,
                        'saidas': saidas,
                        'soma': soma

                    }
                    return render(request, 'pesquisa_saidas.html', context)
                else:
                    saidas = Saida.objects.all().filter(data__month=mes_pes, categoria__id=cat_pes)

                    soma = 0
                    for saida in saidas:
                        soma += saida.valor

                    form = PesquisaForm()
               
                    context = {
                        'form': form,
                        'saidas': saidas,
                        'soma': soma
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

    form = PesquisaForm(request.POST or None)
    if str(request.user) != 'AnonymousUser':

        if str(request.method) == 'POST':
            if form.is_valid():
                pesquisa = form.get_categoria()
                cat_pes = int(pesquisa['cat_pes'])
                mes_pes = int(pesquisa['mes_pes'])


                if (mes_pes == 0 and cat_pes == 0):
                    entradas = Entrada.objects.all()
                    soma = 0
                    for entrada in entradas:
                        soma += entrada.valor

                    form = PesquisaForm()
               
                    context = {
                        'form': form,
                        'entradas': entradas,
                        'soma': soma
                    }
                    return render(request, 'pesquisa_entradas.html', context)
                elif (mes_pes == 0):
                    entradas = Entrada.objects.all().filter(categoria__id=cat_pes)
                    soma = 0
                    for entrada in entradas:
                        soma += entrada.valor
                    form = PesquisaForm()
               
                    context = {
                        'form': form,
                        'entradas': entradas,
                        'soma': soma
                    }
                    return render(request, 'pesquisa_entradas.html', context)
                elif (cat_pes == 0):
                    entradas = Entrada.objects.all().filter(data__month=mes_pes)
                    soma = 0
                    for entrada in entradas:
                        soma += entrada.valor

                    form = PesquisaForm()
               
                    context = {
                        'form': form,
                        'entradas': entradas,
                        'soma': soma
                    }
                    return render(request, 'pesquisa_entradas.html', context)
                else:
                    entradas = Entrada.objects.all().filter(data__month=mes_pes, categoria__id=cat_pes)
                    soma = 0
                    for entrada in entradas:
                        soma += entrada.valor

                    form = PesquisaForm()
               
                    context = {
                        'form': form,
                        'entradas': entradas,
                        'soma': soma
                    }
                    return render(request, 'pesquisa_entradas.html', context)


        form = PesquisaForm()
        context = {
            'form': form
        }
        return render(request, 'pesquisa_entradas.html', context)
    else:
        return redirect('index')