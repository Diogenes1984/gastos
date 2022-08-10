from django.contrib import admin
from .models import Categoria, Entrada, Saida


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(Entrada)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'valor', 'descricao', 'data')
    list_filter = ('categoria', 'data')


@admin.register(Saida)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'valor', 'descricao', 'data')
    list_filter = ('categoria', 'data')