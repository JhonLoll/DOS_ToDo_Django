document.getElementById('action_navbar').innerHTML = `<ul class="nav nav-tabs">
        <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">To-Do - Django</a>
        </li>
        <li class="nav-item dropdown"> 
            <a class="nav-link dropdown-toggle" id="dropdown" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Tarefas</a>
            <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/tarefas/listartarefas">Listar Tarefas</a></li>
            <li><a class="dropdown-item" href="/tarefas/cadastroatividade">Cadastrar Tarefas</a></li>
            </ul>
        </li>
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Usuários</a>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="/tarefas/listarusuarios">Listar Usuários</a></li>
                <li><a class="dropdown-item" href="/tarefas/cadastrarusuario">Cadastrar Usuários</a></li>
            </ul>
        </li>
    </ul>
`;