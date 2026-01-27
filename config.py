import os 
from dotenv import load_dotenv

db_username = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_database = os.getenv('DB_DATABASE')
db_port = os.getenv('DB_PORT')
db_host = os.getenv('DB_HOST')
secret = os.getenv('SECRET_KEY')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'mysql+pymysql://{db_username}:{db_senha}@{db_host}:{db_port}/{db_database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 