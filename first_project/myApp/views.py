from django.shortcuts import render
from .models import Tarefa, Usuario
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# ===========================
# Funções para listar usuários
def listarUsuarios(request):
    
    usuarios = Usuario.objects.all()

    return render(request, "listarusuarios.html", {"usuarios" : usuarios})


# ===========================
# Funções para listar tarefas
def listarTarefas(request):
    
    tarefas = Tarefa.objects.all()

    return render(request, "listartarefas.html", {"tarefas" : tarefas})

def deletarTarefa(request, id):
    
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()

    return HttpResponseRedirect(reverse("listarTarefas"))
