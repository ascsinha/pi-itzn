from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, DateField, RadioField, FileField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa 
from app import db

class EditarPerfildoUsuario(FlaskForm):
    imagem_perfil = FileField('Imagem de perfil')
    email = StringField('E-mail', validators = [DataRequired(), Email()])
    telefone = StringField('Telefone', validators = [DataRequired()])
    enviar = SubmitField('Enviar')