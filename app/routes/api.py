from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from authlib.integrations.flask_client import OAuth
import requests
from config import Config

app = Flask(__name__)


app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


oauth = OAuth(app)

oauth.register(

    name="suap",

    client_id=app.config[
        "SUAP_CLIENT_ID"
    ],

    client_secret=app.config[
        "SUAP_CLIENT_SECRET"
    ],

    # URL de autorização
    authorize_url=
    "https://suap.ifrn.edu.br/o/authorize/",

    # URL de obtenção do token
    access_token_url=
    "https://suap.ifrn.edu.br/o/token/",

    # Escopo solicitado
    client_kwargs={
        "scope": "identificacao"
    }
)
