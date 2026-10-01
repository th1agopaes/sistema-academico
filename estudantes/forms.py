from django import forms
from estudantes.models import Estudante


class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = '__all__'
        widgets = {
            'nascimento': forms.DateInput(
                attrs = {'type': 'date', 'class': 'form-control'},
                format='%Y-%m-%d',
            ),
        }