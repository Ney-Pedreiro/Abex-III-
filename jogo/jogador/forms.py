from django.forms import ModelForm
from django import forms
from .models import Jogador

class JogadorForm(ModelForm):
    class Meta:
        model = Jogador
        fields = '__all__'


