from django import forms

CATEGORIA_CHOICES = (
    (0, 'Todas'),
    (1, 'Croupier'),
    (2, 'Garçom'),
    (3, 'Bebidas'),
    (4, 'Banza'),
    (5, 'Paieiro'),
    (6, 'Larica'),
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

class PesquisaForm(forms.Form):

    cat_pes = forms.ChoiceField(label='Selecione a Categoria', choices=CATEGORIA_CHOICES)

    mes_pes = forms.ChoiceField(label='Selecione a Mês', choices=MES_CHOICES)

    def get_categoria(self):
        cat_pes = self.cleaned_data['cat_pes']
        mes_pes = self.cleaned_data['mes_pes']
        pesquisa = {
            'cat_pes': cat_pes,
            'mes_pes': mes_pes
        }
        return pesquisa

    