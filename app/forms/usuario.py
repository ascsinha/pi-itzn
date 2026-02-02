from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, DateField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa 
from ..models import Usuario
from app import db

class EditarPerfildoUsuario(FlaskForm):
    email = StringField('E-mail', validators = [DataRequired(), Email()])
    telefone = StringField('Telefone', validators = [DataRequired()])
    enviar = SubmitField('Enviar')
    