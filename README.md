# 🧾 API SISPAR - Sistema de Gestão de Colaboradores

Bem-vindo à **API SISPAR**! Esta é uma API RESTful desenvolvida com Flask, que permite gerenciar colaboradores de forma segura e eficiente. Entre as funcionalidades estão o cadastro, listagem, atualização e autenticação de usuários com proteção de senhas.

## 📌 Repositório

🔗 [github.com/Everton-Fernandes/api_sispar](https://github.com/Everton-Fernandes/api_sispar)

---

## 🚀 Tecnologias Utilizadas

- Python 3.12+
- Flask
- SQLAlchemy
- Flasgger (Swagger UI para documentação)

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Everton-Fernandes/api_sispar.git
cd api_sispar
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Como Executar

### 1. Inicie a aplicação

```bash
python run.py
```

Acesse no navegador:

```
http://127.0.0.1:5000/
```

### 1. Acesse a documentação Swagger

```
http://127.0.0.1:5000/apidocs/
```

---

## 🗂 Estrutura do Projeto

```
api_sispar/
├── src/
│   ├── app.py
│   ├── model/
│   │   ├── __init__.py
│   │   └── colaborador_model.py
│   ├── routes/
│   │   └── colaborador_routes.py
│   ├── security/
│   │   └── security.py
│   └── docs/
│       └── colaborador/
│           ├── cadastrar_colaborador.yml
│           ├── pegar_todos_colaboradores.yml
│           ├── atualizar_colaborador.yml
│           └── login.yml
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Autor

Desenvolvido por [Everton Fernandes](https://github.com/Everton-Fernandes) 🚀

---
