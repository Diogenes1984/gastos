from .models import Entrada, Saida


def somaEntradasMeses():



    entradas = Entrada.objects.all()
    aux_jan = 0
    aux_fev = 0
    aux_mar = 0
    aux_abr = 0
    aux_mai = 0
    aux_jun = 0
    aux_jul = 0
    aux_ago = 0
    aux_set = 0
    aux_out = 0
    aux_nov = 0
    aux_dez = 0
    

    for entrada in entradas:
        if entrada.data.year == 2022:

            if entrada.data.month == 1:
                aux_jan += entrada.valor
            elif entrada.data.month == 2:
                aux_fev += entrada.valor
            elif entrada.data.month == 3:
                aux_mar += entrada.valor
            elif entrada.data.month == 4:
                aux_abr += entrada.valor
            elif entrada.data.month == 5:
                aux_mai += entrada.valor
            elif entrada.data.month == 6:
                aux_jun += entrada.valor
            elif entrada.data.month == 7:
                aux_jul += entrada.valor
            elif entrada.data.month == 8:
                aux_ago += entrada.valor
            elif entrada.data.month == 9:
                aux_set += entrada.valor
            elif entrada.data.month == 10:
                aux_out += entrada.valor
            elif entrada.data.month == 11:
                aux_nov += entrada.valor
            elif entrada.data.month == 12:
                aux_dez += entrada.valor

    context = {
        'soma_jan': aux_jan,
        'soma_fev': aux_fev,
        'some_mar': aux_mar,
        'soma_abr': aux_abr,
        'soma_mai': aux_mai,
        'soma_jun': aux_jun,
        'soma_jul': aux_jul,
        'soma_ago': aux_ago,
        'soma_set': aux_set,
        'soma_out': aux_out,
        'soma_nov': aux_nov,
        'soma_dez': aux_dez
    }

    return context
#=======================================================================

def somaSaidaMeses():

    saidas = Saida.objects.all()
    aux_jan = 0
    aux_fev = 0
    aux_mar = 0
    aux_abr = 0
    aux_mai = 0
    aux_jun = 0
    aux_jul = 0
    aux_ago = 0
    aux_set = 0
    aux_out = 0
    aux_nov = 0
    aux_dez = 0

    for saida in saidas:
        if saida.data.year == 2022:

            aux += saida.valor
            if saida.data.month == 1:
                aux_jan += saida.valor
            elif saida.data.month == 2:
                aux_fev += saida.valor
            elif saida.data.month == 3:
                aux_mar += saida.valor
            elif saida.data.month == 4:
                aux_abr += saida.valor
            elif saida.data.month == 5:
                aux_mai += saida.valor
            elif saida.data.month == 6:
                aux_jun += saida.valor
            elif saida.data.month == 7:
                aux_jul += saida.valor
            elif saida.data.month == 8:
                aux_ago += saida.valor
            elif saida.data.month == 9:
                aux_set += saida.valor
            elif saida.data.month == 10:
                aux_out += saida.valor
            elif saida.data.month == 11:
                aux_nov += saida.valor
            elif saida.data.month == 12:
                aux_dez += saida.valor

    context = {
        'soma_jan': aux_jan,
        'soma_fev': aux_fev,
        'some_mar': aux_mar,
        'soma_abr': aux_abr,
        'soma_mai': aux_mai,
        'soma_jun': aux_jun,
        'soma_jul': aux_jul,
        'soma_ago': aux_ago,
        'soma_set': aux_set,
        'soma_out': aux_out,
        'soma_nov': aux_nov,
        'soma_dez': aux_dez
    }

    return context