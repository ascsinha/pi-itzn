from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import Agendamento
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
        observacao = request.form.get('observacao')
        
        novo_agendamento = Agendamento(
            data_reserva = data_reserva,
            hora_inicial = hora_inicial,
            hora_final = hora_final,
            observacao = observacao
        )
        
        if data_reserva.data < date.today():
            raise ValidationError('Você não pode colocar um dia anterior ao de hoje.')
        
        db.session.add(novo_agendamento)
        db.session.commit()
        flash('Agendamento criado com sucesso!', 'success')
        return redirect(url_for('.verAgendamento'))
    return render_template('main/agendamentos.html')
        
@agendamentos.route('/atualizar-agendamento/<int:id>', methods = ['GET', 'POST'])
@login_required
def atualizarAgendamento():
    if current_user.is_authenticated:
        form = EditarAgendamento()
        if form.validate_on_submit():
            Agendamento.data_reserva = form.data_reserva.data
            Agendamento.hora_inicial = form.hora_inicial.data
            Agendamento.hora_final = form.hora_final.data
            db.session.commit()
            flash('Suas modificações foram salvas.', 'success')
            redirect(url_for('.verAgendamento'))
        elif request.method == 'GET':
            form.data_reserva.data = Agendamento.data_reserva
            form.hora_inicial.data = Agendamento.hora_inicial
            form.hora_final.data = Agendamento.hora_final
        return render_template('main/agendamentos.html', form = form)

@agendamentos.route('/ver-agendamento/<int:id>', methods = ['GET'])
@login_required
def verAgendamento(id):
    if current_user.is_authenticated:
        query = Agendamento.query.filter_by(agendamento_id = id).first()
        return render_template('agendamentos/detalhes.html', query = query)

@agendamentos.route('/apagar-agendamento/<int:id>', methods = ['POST'])
@login_required
def apagarAgendamento(id):
    if current_user.is_authenticated:
        agendamento = Agendamento.query.get(id)
        if agendamento is not None:
            db.session.delete(agendamento)
            db.session.commit()
            flash('Agendamento apagado com sucesso!', 'success')
        else:
            flash('O agendamento não foi encontrado', 'danger') 
        return redirect(url_for('.'))
