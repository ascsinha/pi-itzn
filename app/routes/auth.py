from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from ..models import Usuario
import sqlalchemy as sa
from ..forms.auth import LoginForm, RegistrationForm
from app import login_manager
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.agendamentos'))
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email = form.email.data).first()
        if usuario is None and not usuario.checar_senha(form.senha.data):
            flash('E-mail ou senha inválido.')
            return redirect(url_for('auth.login'))
        login_user(usuario)
        return redirect(url_for('index_bp.index'))
    return render_template('auth/login.html', title = 'Log In', form = form)

@auth.route('/cadastro', methods = ['GET', 'POST'])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        nome = request.form.get('nome')
        data_nascimento = request.form.get('data_nascimento')
        cpf = request.form.get('cpf')
        email = request.form.get('email')
        senha = request.form.get('senha')
        Usuario.criar_senha(form.senha.data)
        db.session.commit(nome, data_nascimento, cpf, email, senha)
        db.session.add()
        flash('Parabéns, você é um usuário cadastrado!')
        redirect(url_for('auth.login'))
    return render_template('auth/cadastro.html', title = 'Cadastro', form = form)

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