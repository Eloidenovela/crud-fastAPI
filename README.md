# API

Este repositório contém o código-fonte de uma API web desenvolvida em Python utilizando o framework FastAPI e o banco de dados PostgreSQL. O objetivo do sistema é facilitar a gestão de requerimentos escolares, permitindo que alunos/estudantes e funcionários submetam e acompanhem suas solicitações de maneira eficiente.

## Funcionalidades

- **Criação de Requerimentos:** Alunos/estudantes e funcionários podem criar novos requerimentos.
- **Gerenciamento de Requerimentos:** Administradores podem visualizar, aprovar, rejeitar ou atualizar o status dos requerimentos.
- **Autenticação e Autorização:** Sistema de autenticação para garantir que apenas usuários autorizados possam acessar determinadas funcionalidades.
- **Notificações:** Notifica os usuários sobre o status dos seus requerimentos.

## Tecnologias Utilizadas

- **Linguagem de Programação:** Python
- **Framework Web:** FastAPI
- **Banco de Dados:** PostgreSQL
- **Ferramentas de Gerenciamento de Dependências:** `pip`
- **Servidor de Desenvolvimento:** uvicorn

## Estrutura do Projeto

```
/crud-fastAPI
├── src/
│   ├── main.py
│   ├── models/
│   ├── routers/
│   ├── services/
│   └── controllers/
├── public/
|       ├── img/
|       └── docs/
├── migrations/
├── tests/
├── requirements.txt
└── README.md

```

- **`crud-fastAPI/`**: Contém os arquivos principais do projeto.
  - **`main.py`**: Ponto de entrada da aplicação.
  - **`models/`**: Definições dos modelos de dados.
  - **`routers/`**: Rotas da API.
  - **`services/`**: Lógica de negócios e manipulação de dados.
- **`migrations/`**: Arquivos de migração do banco de dados.
- **`tests/`**: Testes automatizados para a API.
- **`requirements.txt`**: Lista de dependências do projeto.

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- Python 3.8+
- PostgreSQL
- pip (gerenciador de pacotes Python)

## Configuração e Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/eloidenovela/crud-fastAPI.git
   cd crud-fastAPI
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/MacOS
   venv\Scripts\activate     # Para Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados PostgreSQL e atualize as credenciais em `app/database.py`.

5. Execute as migrações para configurar o banco de dados:
   ```bash
   alembic upgrade head
   ```

6. Inicie a aplicação:
   ```bash
   uvicorn app.main:app --reload
   ```

A aplicação estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Testes

Para executar os testes automatizados, utilize o seguinte comando:
```bash
pytest
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
