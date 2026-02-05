from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, login_required
from ..models import Agendamento
from app import db

main = Blueprint('main', __name__)

@main.route('/dashboard')
def dashboard():
    agendamentos = Agendamento.query.order_by(Agendamento.data_reserva.desc()).all()
    return render_template('main/dashboard.html', title = "Dashboard", agendamentos = agendamentos)

@main.route('/perfil')
def perfil():
    return render_template('main/perfil.html', title ="Perfil")

@main.route('/perfil_edit')
def perfil_edit():
    return render_template('main/perfil_edit.html', title ="Perfil")


@main.route('/materiais')
def materiais():
    return render_template('main/materiais.html', title = "Materiais")

@main.route('/dashboard-admin')
def admin():
    return render_template('main/dashboard-admin.html', title = "Dashboard")

@main.route('/modal-agendamentos')
def modal():
    return render_template('main/modal-agendamentos.html', title = "Agendamentos")
