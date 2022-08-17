from django.db import models


class Base(models.Model):
    descricao = models.CharField('Descrição', max_length=50, blank=True)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    data = models.DateField('Data')

    class Meta:
        abstract = True


class CategoriaEntrada(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Cat Entrada'
        verbose_name_plural = 'Cat Entradas'

    def __str__(self):
        return self.nome

class CategoriaSaida(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Cat Saída'
        verbose_name_plural = 'Cat Saídas'

    def __str__(self):
        return self.nome


class Entrada(Base):
    categoria = models.ForeignKey(
        'CategoriaEntrada',
        verbose_name='Categoria',
        on_delete=models.SET_DEFAULT,
        default=1
    )

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.descricao


class Saida(Base):
    categoria = models.ForeignKey(
        'CategoriaSaida',
        verbose_name='Categoria',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Saida'
        verbose_name_plural = 'Saidas'

    def __str__(self):
        return self.descricao

    
class Poupanca(Base):

    class Meta:
        verbose_name = 'Poupança'
        verbose_name_plural = 'Poupança'


    def __str__(self):
        return self.descricao