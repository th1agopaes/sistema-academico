from django import forms
from academico.models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['matricula', 'nome', 'email', 'cpf']
        widgets = {
            'matricula': forms.TextInput(attrs={'class':'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'class':'form-control'}),
        }