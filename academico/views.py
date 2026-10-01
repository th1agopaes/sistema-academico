from django.shortcuts import render
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

    return render(request, 'professores/listagem.html', {'profs':professores})

def criarProfessor(request):
    return render()

def atualizarProfessor(request):
    return render()

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