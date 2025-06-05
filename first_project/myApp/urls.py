from django.urls import path, include
from .views import _login, _logout, _signup, cadastrarUsuario, criarTarefa, deletarUsuario, editarTarefa, listarTarefas, deletarTarefa, listarUsuarios

from rest_framework.routers import DefaultRouter
from .views import TarefaViewSet, UsuarioViewSet

router = DefaultRouter(
    trailing_slash=False
)
router.register(r'tarefas', TarefaViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    # ===========================
    # Funções para listar tarefas
    path('listartarefas/', listarTarefas, name="listarTarefas"),
    path('listartarefas/deletartarefa/<int:id>', deletarTarefa, name="deletarTarefa"),
    path('cadastroatividade/', criarTarefa, name="cadastrarTarefa"),
    path('editaratividade/<int:id>', editarTarefa, name="editarTarefa"),

    # ===========================
    # Funções para listar usuários
    path('listarusuarios/', listarUsuarios, name="listarUsuarios"),
    path('listarusuarios/deletarusuario/<int:id>', deletarUsuario, name="deletarUsuario"),
    path('cadastrarusuario/', cadastrarUsuario, name="cadastrarUsuario"),

    # ===========================
    # Funções para cadastrar / logar usuários
    path('login/', _login, name="login"),
    path('logout/', _logout, name="logout"),
    path('signup/', _signup, name="signup"),
]

urlpatterns += router.urls