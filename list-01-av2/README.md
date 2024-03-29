# Atividade 01 - AV2

Sistema de gerenciamento de produtos com funcionalidades de cadastro de usuário, cadastro de produtos e listagem de produtos utilizando `dict` e `packages`.

## Requisitos

Separar funcionalidades por pacotes com `__init__.py` em pastas `/products/` e `/users/`, no mínimo.

```
.
├── main.py
├── /products/
│   ├── __init__.py
│   ├── listing.py # Listagem de produto
│   └── register.py # Registro de produto
├── /users/
│   ├── __init__.py
│   ├── authentication.py # Autenticação e redirecionamento
│   └── register.py # Registro de usuário
└── /utils/
    ├── __init__.py
    ├── menu.py # Renderização dos menus
    └── validation.py # Validação de informações de usuário
```

