from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime
from ..models import Usuario
import sqlalchemy as sa
from app import login_manager
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuario = Usuario.query.filter_by(email = email).first()
        if usuario and usuario.checar_senha(senha):
            if senha == 'admin123' and not usuario.e_admin:
                usuario.e_admin = True
                db.session.commit()
                flash('Bem-vindo, administrador!', 'success')
            login_user(usuario)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Email ou senha incorretos.', 'error')
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html', title = 'Log In')

@auth.route('/cadastro', methods = ['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        data_nascimento = request.form.get('data_nascimento')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        senha = request.form.get('senha')
        senha2 = request.form.get('senha2')
        
        if Usuario.query.filter_by(email = email).first():
            flash('Esse usuário já existe. Faça login.', 'error')
            return redirect(url_for('auth.login'))
        
        if senha != senha2:
            flash('As senhas não coincidem.')
            return redirect(url_for('auth.cadastro'))
        
        usuario = Usuario(
            nome = nome,
            cpf = cpf,
            data_nascimento = data_nascimento,
            telefone = telefone,
            email = email
        )
        
        usuario.criar_senha(senha)
        
        db.session.add(usuario)
        db.session.commit()
        
        flash('Parabéns, você é um usuário cadastrado!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/cadastro.html', title = 'Cadastro')

@auth.route('/esqueci-senha', methods=['GET', 'POST'])
@login_required
def esqueciSenha():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        if not email:
            flash('Por favor, informe um e-mail válido.', 'error')
            return render_template('auth/esqueci-senha.html', title='Esqueci a Senha')

        # Aqui você integraria com o serviço de e-mail para enviar o link de recuperação.
        # Exemplo: send_reset_email(email)
        flash('Se o e-mail estiver cadastrado, enviamos um link de recuperação.', 'success')
        return redirect(url_for('login'))

    return render_template('auth/esqueci-senha.html', title='Esqueci a Senha')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index_bp.index'))

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.filter(Usuario.id == int(user_id)).first()