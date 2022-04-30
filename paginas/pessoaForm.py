from django import forms
from models import Pessoa

class PessoaForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Pessoa
        fields = '__All__'
