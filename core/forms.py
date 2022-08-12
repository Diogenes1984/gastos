from django import forms

CATEGORIA_CHOICES = (
    (1, 'Croupier'),
    (2, 'Garçom'),
    (3, 'Bebidas'),
    (4, 'Banza'),
    (5, 'Paieiro'),
    (6, 'Larica'),
)

class PesquisaForm(forms.Form):

    pesquisa = forms.ChoiceField(
        choices=CATEGORIA_CHOICES
    )

    def get_categoria(self):
        pesquisa = self.cleaned_data['pesquisa']
        return pesquisa