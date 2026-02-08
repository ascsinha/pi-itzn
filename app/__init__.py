from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Você deve estar logado para acessar esta página.'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    from .routes.auth import auth
    app.register_blueprint(auth)
    
    from .routes.main import main
    app.register_blueprint(main)
    
    from .routes.index_bp import index_bp
    app.register_blueprint(index_bp)
    
    from .routes.agendamentos import agendamentos
    app.register_blueprint(agendamentos)
    
    return app 