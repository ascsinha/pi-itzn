from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()

migrate = Migrate()
# login = LoginManager()
# login.login_view = 'auth.login'
# login.login_message = 'Você deve estar logado para acessar esta página.'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    # login.init_app(app)
    
    from .routes.auth import auth
    app.register_blueprint(auth)
    
    from .routes.main import main
    app.register_blueprint(main)
    
    from .routes.usuario import usuario
    app.register_blueprint(usuario)
    
    from .routes.index_bp import index_bp
    app.register_blueprint(index_bp)
    
    from .routes.agendamentos import agendamentos
    app.register_blueprint(agendamentos)
    
    return app 
