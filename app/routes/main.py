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
    usuario = Usuario.query.get(current_user.id)
    return render_template('main/perfil.html', title ="Perfil", usuario = usuario)

@main.route('/perfil_edit/<int:id>', methods = ['GET', 'POST'])
@login_required
def perfil_edit(id):
    usuario = Usuario.query.get(current_user.id)
    
    if request.method == 'POST':
        usuario.email = request.form.get('email')
        usuario.telefone = request.form.get('telefone')
        
        db.session.add(usuario)
        db.session.commit()
        flash('Suas modificações foram salvas!', 'success')
        return redirect(url_for('.perfil', id = usuario.id))
    return render_template('main/perfil_edit.html', title ="Editar Perfil", usuario = usuario)

@main.route('/materiais')
@login_required
def materiais():
    return render_template('main/materiais.html', title = "Materiais")

@main.route('/dashboard-admin')
def admin():
    return render_template('main/dashboard-admin.html', title = "Dashboard")

@main.route('/modal-agendamentos')
def modal():
    return render_template('main/modal-agendamentos.html', title = "Agendamentos")

@main.route('/configuracoes')
def configuracoes():
    return render_template('main/configuracoes.html', title= "Configuracao")
