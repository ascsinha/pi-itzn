from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import Agendamento, Usuario
from app import db, Config

main = Blueprint('main', __name__)

@main.route('/dashboard', methods = ['GET'])
@login_required
def dashboard():
    page = int(request.args.get('page', 1))
    agendamentos = Agendamento.query.filter_by(id_usuario=current_user.id).order_by(Agendamento.data_reserva.desc())
    agends_pagina = db.paginate(agendamentos, page=page, per_page=Config.AGENDS_POR_PAGINA, error_out=False)
    next_url = url_for('main.dashboard', page=agends_pagina.next_num) if agends_pagina.has_next else None
    prev_url = url_for('main.dashboard', page=agends_pagina.prev_num) if agends_pagina.has_prev else None
    return render_template('main/dashboard.html', title = "Dashboard", page=page, agendamentos = agends_pagina.items, posts=agends_pagina.items, next_url=next_url, prev_url=prev_url)

@main.route('/dashboard-admin', methods = ['GET'])
@login_required
def dashboard_admin():
    return render_template('main/dashboard-admin.html', title = "Dashboard - Admin", page=page, agendamentos = agends_pagina.items, posts=agends_pagina.items, next_url=next_url, prev_url=prev_url)


@main.route('/perfil/<int:id>')
@login_required
def perfil(id):
    usuario = Usuario.query.get_or_404(id)
    return render_template('main/perfil.html', title ="Perfil", usuario = usuario)

@main.route('/perfil_edit/<int:id>')
@login_required
def perfil_edit(id):
    return render_template('main/perfil_edit.html', title ="Editar Perfil")

@main.route('/materiais')
@login_required
def materiais():
    return render_template('main/materiais.html', title = "Materiais")
