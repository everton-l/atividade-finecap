from django import forms
from .models import *

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'cnpj': forms.TextInput(attrs={'class':'form-control'}),
            'nome_emopresa': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_empresa': forms.TextInput(attrs={'class':'form-control'}),
            'quitado': forms.CheckboxInput(attrs={'class':'form-control'}),
            'stand': forms.Select(attrs={'class':'form-control'})
        }

