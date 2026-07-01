from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from authlib.integrations.flask_client import OAuth
from config import Config
import os

# Extensões
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
oauth = OAuth()

login_manager.login_view = "auth.login"
login_manager.login_message = "Você deve estar logado para acessar esta página."


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa as extensões
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    oauth.init_app(app)

    # Configuração do OAuth do SUAP
    oauth.register(
        name="suap",
        client_id=app.config["SUAP_CLIENT_ID"],
        client_secret=app.config["SUAP_CLIENT_SECRET"],
        authorize_url="https://suap.ifrn.edu.br/o/authorize/",
        access_token_url="https://suap.ifrn.edu.br/o/token/",
        client_kwargs={
            "scope": "identificacao"
        }
    )

    # Blueprints
    from .routes.auth import auth
    app.register_blueprint(auth)

    from .routes.main import main
    app.register_blueprint(main)

    from .routes.index_bp import index_bp
    app.register_blueprint(index_bp)

    from .routes.agendamentos import agendamentos
    app.register_blueprint(agendamentos)

    return app