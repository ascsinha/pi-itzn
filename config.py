import os 
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path=os.path.join(basedir, ".env"))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    UPLOAD_EXTENSIONS = ['.png', '.jpeg', '.jpg', '.gif', '.webp']
    AGENDS_POR_PAGINA = 3
    
    SUAP_CLIENT_ID = os.getenv("SUAP_CLIENT_ID")
    SUAP_CLIENT_SECRET = os.getenv("SUAP_CLIENT_SECRET")
    