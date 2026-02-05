from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from ..models import Agendamento, Status
from wtforms.validators import ValidationError
from ..forms.agendamentos import CriarAgendamento, EditarAgendamento
from datetime import date
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
        
        agendamento = Agendamento(
            data_reserva = data_reserva,
            hora_inicial = hora_inicial,
            hora_final = hora_final,
            id_estacao = id_estacao,
            observacao = observacao,
            validacao = Status.EM_ANALISE
        )
        
        if data_reserva.data < date.today():
            raise ValidationError('Você não pode colocar um dia anterior ao de hoje.')
        
        db.session.add(agendamento)
        db.session.commit()
        flash('Agendamento criado com sucesso!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('main/agendamentos.html', title = 'Agendar')
        
@agendamentos.route('/atualizar-agendamento/<int:id>', methods = ['GET', 'POST'])
@login_required
def atualizarAgendamento(id):
    if request.method == 'POST':
        agendamento = Agendamento.query.get(id)
        agendamento.data_reserva = request.form.get('data_reserva')
        agendamento.hora_inicial = request.form.get('hora_inicial')
        agendamento.hora_final = request.form.get('hora_final')
        agendamento.observacao = request.form.get('observacao')
        
        db.session.add(agendamento)
        db.session.commit()
        flash('Suas modificações foram salvas!', 'success')
        redirect(url_for('.verAgendamento'))
        
    elif request.method == 'GET':
        data_reserva = Agendamento.data_reserva
        form.hora_inicial.data = Agendamento.hora_inicial
        form.hora_final.data = Agendamento.hora_final
    return render_template('main/agendamentos.html', title = 'Editar Agendamento', agendamento = agendamento)

@agendamentos.route('/ver-agendamento/<int:id>', methods = ['GET'])
@login_required
def verAgendamento(id):
    if request.method == 'GET':
        query = Agendamento.query.filter_by(agendamento_id = id).first()
        return render_template('agendamentos/detalhes.html', query = query, title = 'Detalhes do Agendamento')

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
        return redirect(url_for('.'))
