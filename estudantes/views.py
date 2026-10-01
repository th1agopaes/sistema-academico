from django.shortcuts import redirect, render
from django.http import HttpResponse

from estudantes.forms import EstudanteForm
from estudantes.models import Estudante

#-- O arquivo views é onde definimos as nossas regras de negocios

#-- método/função para listagem
#-- de estudantes

#-- regra de negócio para adicionar estudante
def criarEstudante(request):
    form = EstudanteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    dicionario = {
        'form' : form
    }

    return render(request, 'estudantes/adicionar.html', dicionario)

def listarEstudantes(request):
    estudante = Estudante.objects.all()
    contexto = {
        'estudantes' : estudante,
    }

    return render(request, 'estudantes/listagem.html', contexto)

def deletarEstudante(request, pk):
    estudante = Estudante.objects.get(pk=pk)
    estudante.delete()
    return redirect('/')

def atualizarEstudante(request, pk):
    editar = Estudante.objects.get(pk=pk)

    edicao = EstudanteForm(request.POST or None, request.FILES or None, instance=editar)
    if edicao.is_valid():
        edicao.save()
        return redirect('/')

    dicionario = {
        'form' : edicao
    }

    return render(request, 'estudantes/adicionar.html', context=dicionario)