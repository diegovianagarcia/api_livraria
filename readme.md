# Developer Backend Challenge

## Desafio
Digamos que você trabalha para uma Livraria Online, onde é possível verificar todos dados dos livros que você pegou emprestado ou livros que gostaria de realizar uma reserva. Nosso tempo de reserva do livro é 3 dias.

## Algumas funcionalidades 
- Cadastrar o livro
- Cadastrar o cliente
- Realizar a reserva de um livro para o cliente
- Listar todos os livros cadastrados e também o seu status, “disponível” ou “emprestado”
- Listar os livros emprestados ao cliente calculando multa e juros de acordo com a tabela abaixo:

| Dias em atraso | Multa | Juros ao Dia |
| ------ | ------ | ------ |
| Sem atraso | 0% | 0% |
| Até 3 dias | 3% | 0.2% |
| Acima 3 dias | 5% | 0.4% |
| Acima 5 dias | 7% | 0.6% |

## Ambiente de desenvolvimento
Principais dependências:

![](https://img.shields.io/badge/Python-v3.7+-green)
![](https://img.shields.io/badge/Django-v2.2.5-green)
![](https://img.shields.io/badge/django_filter-v2.2.0-green)
![](https://img.shields.io/badge/djangorestframework-v3.9.4-green)
![](https://img.shields.io/badge/drf_nested_routers-v0.91-green)

Pré-requisitos:

- Python na versão especificada no projeto, baixar e instalar em:
  
> [Windows](https://www.python.org/downloads/windows/)

> [Mac](https://www.python.org/downloads/mac-osx/)

> [Linux](https://www.python.org/downloads/source/)

Acessar o fonte projeto:

``cd  api_livraria``

Criação da virtualenv para isolar a instalação das dependências:

``python -m venv .venv``

Ativação da virtualenv:

``source .venv/bin/activate``

Realizar a instalação das dependências do projeto:

``pip install -r requirements.txt``

Realizar a migração do banco de dados

``cd src`` 

``python manage.py migrate``

Configurar as variáveis de ambiente

| Variável    | Descrição           | Default
| ----------- | ------------------- |----
| VALUE_LENT  | Valor do emprestimo | 10.00
| DAYS_LENT   | Dias de emprestimo  | 3
---

Neste momento, basta rodar o projeto

``python manage runserver``

Para executar testes unitários

``python manage.py test v1.tests``

## Endpoints disponíveis:
- /v1/client
- /v1/client/{id}/book
- /v1/book
- /v1/book{id}/reserve
