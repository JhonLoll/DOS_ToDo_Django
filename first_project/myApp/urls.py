from django.urls import path, include
from .views import cadastrarUsuario, criarTarefa, deletarUsuario, editarTarefa, listarTarefas, deletarTarefa, listarUsuarios

urlpatterns = [
    path('listartarefas/', listarTarefas),
    path('listartarefas/deletartarefa/<int:id>', deletarTarefa),
    path('cadastroatividade/', criarTarefa),
    path('editaratividade/<int:id>', editarTarefa),

    path('listarusuarios/', listarUsuarios),
    path('listarusuarios/deletarusuario/<int:id>', deletarUsuario),
    path('cadastrarusuario/', cadastrarUsuario),
]
