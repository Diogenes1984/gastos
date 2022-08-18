from django.contrib import admin
from .models import CategoriaEntrada, CategoriaSaida, Entrada, Saida, Poupanca


@admin.register(CategoriaEntrada)
class CategoriaEntradaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(CategoriaSaida)
class CategoriaSaidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(Entrada)
class CategoriaAdmin(admin.ModelAdmin):
    fields = ['categoria', 'valor', 'data', 'descricao']
    list_display = ('id', 'categoria', 'valor', 'data', 'descricao')
    list_filter = ('categoria', 'data')
    


@admin.register(Saida)
class CategoriaAdmin(admin.ModelAdmin):
    fields = ['categoria', 'valor', 'data', 'descricao']
    list_display = ('id', 'categoria', 'valor', 'data', 'descricao')
    list_filter = ('categoria', 'data')


@admin.register(Poupanca)
class PoupancaAdmin(admin.ModelAdmin):
    list_display = ('id', 'valor', 'descricao', 'data')
    list_filter = ('valor', 'data')