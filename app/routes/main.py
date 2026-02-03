from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, login_required
from ..models import Agendamento
from app import db

main = Blueprint('main', __name__)

@main.route('/agendamentos')
def agendamentos():
    return render_template('main/agendamentos.html', title = "Agendamentos")

@main.route('/dashboard')
def dashboard():
<<<<<<< HEAD
    return render_template('main/dashboard.html', title = "Dashboard")

@main.route('/perfil')
def perfil():
    return render_template('main/perfil.html', title ="Perfil")
=======
    agendamentos = Agendamento.query.order_by(Agendamento.data_reserva.desc()).all()
    return render_template('main/dashboard.html', title = "Dashboard", agendamentos = agendamentos)
>>>>>>> acsa
