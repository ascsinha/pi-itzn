from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from ..models import Agendamento
from app import db

agendamentos = Blueprint('agendamentos', __name__, url_prefix = '/agendamentos')

@agendamentos.route('/agendamentos', methods = ['GET'])
def index():
    agendamentos = Agendamento.query.order_by(Agendamento.data_reserva.desc()).all()
    return render_template('agendamentos/agendamentos.html', agendamentos = agendamentos)

@agendamentos.route('/criar-agendamento', methods = ['GET', 'POST'])
@login_required
def criarAgendamento():
    novo_agendamento = Agendamento()
    db.session.add(novo_agendamento)
    db.session.commit()
    flash('Agendamento criado com sucesso!')
    return redirect(url_for(''))
    
@agendamentos.route('/atualizar-agendamento/<int:id>', methods = ['GET', 'POST'])
@login_required
def atualizarAgendamento():
    form = EditarAgendamento()
    if form.validate_on_submit():
        Agendamento.data = form.data_reserva.data
        db.session.commit()
        flash('Suas modificações foram salvas.')
        redirect(url_for('.verAgendamento'))
    elif request.method == 'GET':
        form.data_reserva.data = Agendamento.data_reserva
    return render_template('atualizarAgendamento.html', form = form)

@agendamentos.route('/ver-agendamento/<int:id>', methods = ['GET'])
@login_required
def verAgendamento(id):
    query = Agendamento.query.filter_by(agendamento_id = id).first()
    return render_template('agendamentos/detalhes.html', query = query)

@agendamentos.route('/apagar-agendamento/<int:id>', methods = ['POST'])
@login_required
def apagarAgendamento(id):
    agendamento = Agendamento.query.get(id)
    if agendamento is not None:
        db.session.delete(agendamento)
        db.session.commit()
        flash('Agendamento apagado com sucesso!', 'success')
    else:
        flash('O agendamento não foi encontrado', 'danger') 
    return redirect(url_for('.'))
