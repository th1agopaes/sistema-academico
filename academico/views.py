from django.shortcuts import render, redirect, get_object_or_404
from academico.forms import ProfessorForm
from academico.models import Curso, Disciplina, Professor, Turma

# Create your views here.

# ----------- Dashboard
def dashboard(request):
    return render(request, 'dashboard.html')

# ----------- Professor
def listarProfessores(request):
    #obtêm todas as instâncias com todos os registros
    #-- dos professores
    professores = Professor.objects.all()

    return render(request, 'academico/professores/listagem.html', {'profs':professores},)

def criarProfessor(request):
    form = ProfessorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('professor_listar')

    return render(request, 'academico/professores/adicionar.html', {'form':form},)

def atualizarProfessor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    form = ProfessorForm(request.POST or None, instance=professor)

    if form.is_valid():
        form.save()
        return redirect('professor_listar')
    return render(request, 'academico/professores/adicionar.html', {'form':form})

def deletarProfessor(request):
    return render()
# ----------- Curso
def listarCursos(request):
    cursos = Curso.objects.all()

    return render(request, 'cursos/listagem.html', {'curs':cursos})

def criarCurso(request):
    return render()

def atualizarCurso(request):
    return render()

def deletarCurso(request):
    return render()

# ----------- Turma
def listarTurmas(request):
    turmas = Turma.objects.all()

    return render(request, 'turmas/listagem.html', {'turms':turmas})

def criarTurma(request):
    return render()

def atualizarTurma(request):
    return render()

def deletarTurma(request):
    return render()

# ----------- Disciplina
def listarDisciplinas(request):
    disciplinas = Disciplina.objects.all()

    return render(request, 'disciplinas/listagem.html', {'discipls':disciplinas})

def criarDisciplina(request):
    return render()

def atualizarDisciplina(request):
    return render()

def deletarDisciplina(request):
    return render()