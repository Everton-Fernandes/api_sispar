from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.model import db
from config import Config
from flask_cors import CORS  # type: ignore
from flasgger import Swagger  # type: ignore

swagger_config = {
    "headers": [],  # cabeçalhos da requisição
    "specs": [  # especificações da API lista + dicionário [{}]
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
}


def create_app():
    app = Flask(__name__)
    CORS(app, origins="*")  # ativa o cors para todas as rotas
    app.register_blueprint(bp_colaborador)
    app.config.from_object(Config)
    db.init_app(app)  # Inicializa o banco de dados com a aplicação Flask
    Swagger(
        app, config=swagger_config
    )  # Inicializa o Swagger e adiciona a configuração
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados se não existirem
    return app
