from flask import Flask
import os

app = Flask(__name__)

# Use an environment variable for SECRET_KEY in production; fallback for local dev
app.config['SECRET_KEY'] = os.environ.get('ITZN_SECRET_KEY', 'dev-secret-key')

from app import routes