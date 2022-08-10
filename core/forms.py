from dataclasses import fields
from django.forms import ModelForm
from .models import Entrada


class PesquisaForm(ModelForm):
    class Meta:
        model = Entrada
        fields = ['categoria', 'data']

    
