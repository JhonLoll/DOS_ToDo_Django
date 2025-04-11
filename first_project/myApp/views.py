import datetime
from re import split
from django.shortcuts import redirect, render
from .models import Tarefa, Usuario
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# ===========================
# Funções para listar usuários
def listarUsuarios(request):
    
    usuarios = Usuario.objects.all()

    return render(request, "listarusuarios.html", {"usuarios" : usuarios})

def deletarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()

    return HttpResponseRedirect("/tarefas/listarusuarios/")

def cadastrarUsuario(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario.save()

        # Encaminha o usuário para a lista de usuários
        return HttpResponseRedirect("/tarefas/listarusuarios/")

    return render(request, "cadastrousuario.html")


# ===========================
# Funções para listar tarefas
def listarTarefas(request):
    
    tarefas = Tarefa.objects.all()

    return render(request, "listartarefas.html", {"tarefas" : tarefas})

def deletarTarefa(request, id):
    
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()

    return HttpResponseRedirect("/tarefas/listartarefas/")

def criarTarefa(request):

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        # dia = request.POST.get("data").split("-")[0]
        # mes = request.POST.get("data").split("-")[1]
        # ano = request.POST.get("data").split("-")[2]
        data = request.POST.get("data")
        usuario = Usuario.objects.get(id=request.POST.get("usuario"))

        # data = datetime.datetime(int(ano), int(mes), int(dia))

        tarefa = Tarefa(titulo=titulo, descricao=descricao, data=data, usuario=usuario)
        tarefa.save()

        # Encaminha o usuário para a lista de tarefas
        return HttpResponseRedirect("/tarefas/listartarefas/")

    usuarios = Usuario.objects.all()

    return render(request, "cadastroatividade.html", {"usuarios" : usuarios})

def editarTarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        data = request.POST.get("data")
        usuario = Usuario.objects.get(id=request.POST.get("usuario"))

        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.data = data
        tarefa.usuario = usuario

        tarefa.save()

        return HttpResponseRedirect("/tarefas/listartarefas/")

    usuarios = Usuario.objects.all()

    return render(request, "editaratividade.html", {"tarefa" : tarefa, "usuarios" : usuarios})
