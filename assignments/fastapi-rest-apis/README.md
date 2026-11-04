# 📘 Atividade: APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando o framework FastAPI. Pratique rotas HTTP, validação de dados com modelos Pydantic, respostas JSON e códigos de status.

## 📝 Tarefas

### 🛠️ Criar a aplicação e listar tarefas

#### Descrição
Prepare o ambiente, execute a aplicação inicial e implemente um endpoint para consultar as tarefas armazenadas em memória.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi uvicorn`.
- Iniciar a aplicação com `uvicorn starter-code:app --reload`.
- Implementar `GET /tasks` para retornar a lista de tarefas em JSON, inclusive quando estiver vazia.
- Permitir que a documentação interativa da API seja acessada em `/docs`.

### 🛠️ Criar tarefas com validação

#### Descrição
Implemente um endpoint para criar tarefas. Use o modelo Pydantic fornecido para validar os dados recebidos no corpo da requisição.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` aceitando um título e, opcionalmente, o estado `completed`.
- Rejeitar dados inválidos usando a validação do modelo Pydantic.
- Atribuir um identificador único e crescente a cada tarefa criada.
- Retornar a tarefa criada em JSON com o código de status `201 Created`.

### 🛠️ Consultar, atualizar e remover tarefas

#### Descrição
Implemente as operações de consulta, atualização e remoção de uma tarefa específica usando seu identificador na URL.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para retornar uma tarefa ou `404 Not Found` quando ela não existir.
- Implementar `PUT /tasks/{task_id}` para atualizar os dados da tarefa e retornar o registro atualizado.
- Implementar `DELETE /tasks/{task_id}` para remover a tarefa e retornar `204 No Content`.
- Retornar `404 Not Found` nas operações de atualização ou remoção quando o identificador não existir.
