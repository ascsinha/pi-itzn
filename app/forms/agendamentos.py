from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, DateField, RadioField, TimeField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa 
from app import db

class CriarAgendamento(FlaskForm):
    estacao = RadioField('Escolha uma das estações disponíveis:', validators = [DataRequired()])
    data_reserva = DateField('Escolha a data da sua reserva', format = '%D/%M/%Y')
    hora_inicial = TimeField('Hora-inicial', format = '%H:%M')
    hora_final = TimeField('Hora-final', format = '%H:%M')
    enviar = SubmitField('Enviar')

class EditarAgendamento(FlaskForm):
    estacao = RadioField('Escolha uma das estações disponíveis:', validators = [DataRequired()])
    data_reserva = DateField('Escolha a data da sua reserva', format = '%D/%M/%Y')
    hora_inicial = TimeField('Hora-inicial', format = '%H:%M')
    hora_final = TimeField('Hora-final', format = '%H:%M')
    enviar = SubmitField('Enviar')
    