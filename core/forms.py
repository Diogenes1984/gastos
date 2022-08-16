from django import forms

CATEGORIA_CHOICES = (
    (0, 'Todas'),
    (1, 'Garçom'),
    (2, 'Croupier'),
    (3, 'Banza'),
    (4, 'CNH'),
    (5, 'Larica'),
    (6, 'Bebidas'),
    (7, 'Paieiro'),
    (8, 'Faculdade'),
    (9, 'Celular'),
    (10, 'Transporte'),
    (11, 'Acessórios/Equipamentos'),
)

MES_CHOICES = (
    (0, 'Todos'),
    (1, 'Janeiro'),
    (2, 'Fevereiro'),
    (3, 'Março'),
    (4, 'Abril'),
    (5, 'Maio'),
    (6, 'Junho'),
    (7, 'Julho'),
    (8, 'Agosto'),
    (9, 'Setembro'),
    (10, 'Outubro'),
    (11, 'Novembro'),
    (12, 'Dezembro'),
)

ANO_CHOICES = (
    (0, 'Todos'),
    (2022, '2022'),
    (2023, '2023'),
    (2024, '2024'),
    (2025, '2025'),
)

class PesquisaForm(forms.Form):

    cat_pes = forms.ChoiceField(label='Selecione a Categoria', choices=CATEGORIA_CHOICES)

    mes_pes = forms.ChoiceField(label='Selecione o Mês', choices=MES_CHOICES)

    def get_categoria(self):
        cat_pes = self.cleaned_data['cat_pes']
        mes_pes = self.cleaned_data['mes_pes']
        pesquisa = {
            'cat_pes': cat_pes,
            'mes_pes': mes_pes
        }
        return pesquisa

class PoupancaForm(forms.Form):
    
    mes_pes = forms.ChoiceField(label='Selecione o Mês', choices=MES_CHOICES)

    def get_poupanca(self):
        mes_pes = self.cleaned_data['mes_pes']
        pesquisa = {
            'mes_pes': mes_pes
        }
        return pesquisa

class RelatorioForm(forms.Form):
    ano_pes = forms.ChoiceField(label='Escolha o ano do relatório', choices=ANO_CHOICES)

    def get_ano(self):
        ano_pes = self.cleaned_data['ano_pes']
        pesquisa = {
            'ano_pes': ano_pes
        }
        return pesquisa