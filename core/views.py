from django.shortcuts import render, redirect
from .models import Categoria, Entrada, Saida, Poupanca
from .utils import somaEntradasMeses, somaSaidaMeses
from .forms import PesquisaForm, PoupancaForm, RelatorioForm

def index(request):

    form = RelatorioForm(request.POST or None)
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            if form.is_valid():
                pesquisa = form.get_ano()
                ano_pes = int(pesquisa['ano_pes'])

                if (ano_pes == 0):
                    entradas = Entrada.objects.all()
                    soma_entradas = 0
                    for entrada in entradas:
                        soma_entradas += entrada.valor
                    
                    saidas = Saida.objects.all()
                    soma_saidas = 0
                    for saida in saidas:
                        soma_saidas += saida.valor

                    poupanca = Poupanca.objects.all()
                    soma_poupanca = 0
                    for poup in poupanca:
                        soma_poupanca += poup.valor
                    
                    
                    saldo = soma_entradas - soma_saidas
                    form = RelatorioForm()

                    context = {
                        'logado': True,
                        'form': form,
                        'entradas': entradas,
                        'saidas': saidas,
                        'poupanca': poupanca,
                        'soma_entradas': soma_entradas,
                        'soma_saidas': soma_saidas,
                        'soma_poupanca': soma_poupanca,
                        'saldo': saldo,
                        'ano_pes': ano_pes
                    }
                    return render(request, 'index.html', context)
                else:
                    entradas = Entrada.objects.all().filter(data__year=ano_pes)
                    soma_entradas = 0
                    for entrada in entradas:
                        soma_entradas += entrada.valor
                    
                    saidas = Saida.objects.all().filter(data__year=ano_pes)
                    soma_saidas = 0
                    for saida in saidas:
                        soma_saidas += saida.valor

                    poupanca = Poupanca.objects.all().filter(data__year=ano_pes)
                    soma_poupanca = 0
                    for poup in poupanca:
                        soma_poupanca += poup.valor

                    saldo = soma_entradas - soma_saidas
                    form = RelatorioForm()
                    context = {
                        'logado': True,
                        'form': form,
                        'entradas': entradas,
                        'saidas': saidas,
                        'poupanca': poupanca,
                        'soma_entradas': soma_entradas,
                        'soma_saidas': soma_saidas,
                        'soma_poupanca': soma_poupanca,
                        'saldo': saldo,
                        'ano_pes': ano_pes
                    }
                    return render(request, 'index.html', context)
        form = RelatorioForm()
        logado = True
        context = {
            'logado': logado,
            'form': form
        }
        return render(request, 'index.html', context)

    else:
        form = RelatorioForm()
        titulo = 'WARNING'
        context = {
            'form': form,
            'titulo': titulo
        }
        return render(request, 'index.html', context)


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

def poupanca(request):
    form = PoupancaForm(request.POST or None)
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            if form.is_valid():
                pesquisa = form.get_poupanca()
                mes_pes = int(pesquisa['mes_pes'])

                if (mes_pes == 0):
                    poupanca = Poupanca.objects.all()
                    soma = 0
                    for poup in poupanca:
                        soma += poup.valor

                    form = PoupancaForm()

                    context = {
                        'form': form,
                        'poupanca': poupanca,
                        'soma': soma
                    }
                    return render(request, 'poupanca.html', context)
                else:
                    poupanca = Poupanca.objects.all().filter(data__month=mes_pes)
                    soma = 0
                    for poup in poupanca:
                        soma += poup.valor

                    form = PoupancaForm

                    context = {
                        'form': form,
                        'poupanca': poupanca,
                        'soma': soma
                    }
                    return render(request, 'poupanca.html', context)
        form = PoupancaForm()
        context = {
            'form': form
        }
        return render(request, 'poupanca.html', context)

    else:
        return redirect('index')