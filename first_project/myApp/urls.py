from django.urls import path, include
from .views import listarTarefas, deletarTarefa, listarUsuarios

urlpatterns = [
    path('listartarefas/', listarTarefas),
    path('deletartarefa/<int:id>/', deletarTarefa),

    path('listarusuarios/', listarUsuarios),
]
