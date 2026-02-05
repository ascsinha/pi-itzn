from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import Agendamento, Status
from wtforms.validators import ValidationError
from datetime import datetime, date
from app import db

agendamentos = Blueprint('agendamentos', __name__, url_prefix = '/agendamentos')

@agendamentos.route('/criar-agendamento', methods = ['GET', 'POST'])
@login_required
def criarAgendamento():
    if request.method == 'POST':
        data_reserva = request.form.get('data_reserva')
        hora_inicial = request.form.get('hora_inicial')
        hora_final = request.form.get('hora_final')
        id_estacao = request.form.get('id_estacao')
        observacao = request.form.get('observacao')
        
        data_reserva_dt = datetime.strptime(data_reserva, '%Y-%m-%d').date()
        if data_reserva_dt < date.today():
            flash('Você não pode colocar um dia anterior ao de hoje.')
            return redirect(url_for('agendamentos.criarAgendamento'))
        
        agendamento = Agendamento(
            id_usuario = current_user.id,
            data_reserva = data_reserva_dt,
            hora_inicial = hora_inicial,
            hora_final = hora_final,
            id_estacao = int(id_estacao),
            observacao = observacao,
            validacao = Status.EM_ANALISE
        )
        
        db.session.add(agendamento)
        db.session.commit()
        flash('Agendamento criado com sucesso!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('main/agendamentos.html', title = 'Agendar')
        
@agendamentos.route('/atualizar-agendamento/<int:id>', methods = ['GET', 'POST'])
@login_required
def atualizarAgendamento(id):
    agendamento = Agendamento.query.get(id)
    
    if request.method == 'POST':
        agendamento.data_reserva = request.form.get('data_reserva')
        agendamento.hora_inicial = request.form.get('hora_inicial')
        agendamento.hora_final = request.form.get('hora_final')
        agendamento.id_estacao = request.form.get('id_estacao')
        agendamento.observacao = request.form.get('observacao')
        
        db.session.add(agendamento)
        db.session.commit()
        flash('Suas modificações foram salvas!', 'success')
        return redirect(url_for('.verAgendamento'))
        
    return render_template('main/atualizar_agendamento.html', title = 'Editar Agendamento', agendamento = agendamento)

@agendamentos.route('/ver-agendamento/<int:id>', methods = ['GET'])
@login_required
def verAgendamento(id):
    if request.method == 'GET':
        agendamento = Agendamento.query.filter_by(id_agendamento = id).first()
        data_reserva = agendamento.data_reserva
        hora_inicial = agendamento.hora_inicial
        hora_final = agendamento.hora_final
        id_estacao = agendamento.id_estacao
        observacao = agendamento.observacao
    return render_template('main/ver_agendamento.html', title = 'Detalhes do Agendamento', agendamento = agendamento, data_reserva=data_reserva, hora_inicial=hora_inicial, hora_final=hora_final, id_estacao=id_estacao, observacao = observacao)

@agendamentos.route('/apagar-agendamento/<int:id>', methods = ['POST'])
@login_required
def apagarAgendamento(id):
    if request.method == 'POST':
        agendamento = Agendamento.query.get(id)
        if agendamento is not None:
            db.session.delete(agendamento)
            db.session.commit()
            flash('Agendamento apagado com sucesso!', 'success')
        else:
            flash('O agendamento não foi encontrado', 'danger') 
        return redirect(url_for('main.dashboard'))
