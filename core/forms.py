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
            'stand': forms.Select(attrs={'class':'form-control'}),
            'data': forms.DateInput(attrs={'class':'form-control'})
        }

class FiltroReservaForm(forms.Form):
    nome_empresa = forms.CharField(label='Nome da Empresa', required=False)
    quitado = forms.BooleanField(label='Quitado', required=False)
    valor_stand = forms.DecimalField(label='Valor do Stand', required=False, min_value=0.00)
    data_reserva = forms.DateField(label='Data da Reserva', required=False)