from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from ..models import Agendamento, Usuario
from app import db

main = Blueprint('main', __name__)

@main.route('/dashboard', methods = ['GET'])
@login_required
def dashboard():
    agendamentos = Agendamento.query.order_by(Agendamento.data_reserva.desc()).all()
    return render_template('main/dashboard.html', title = "Dashboard", agendamentos = agendamentos)

@main.route('/perfil/<int:id>')
@login_required
def perfil(id):
    usuario = Usuario.query.get_or_404(id)
    return render_template('main/perfil.html', title ="Perfil", usuario = usuario)

@main.route('/perfil_edit/<int:id>')
@login_required
def perfil_edit(id):
    return render_template('main/perfil_edit.html', title ="Perfil")

@main.route('/materiais')
@login_required
def materiais():
    return render_template('main/materiais.html', title = "Materiais")