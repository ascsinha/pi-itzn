import os 
from dotenv import load_dotenv

db_senha = os.getenv('DB_PASSWORD')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'da**1D23%342@J$knni&&21'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'mysql+pymysql://app_user:{db_senha}@fases.site:3308/pi2025_itzn'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    