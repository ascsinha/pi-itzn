from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from ..models import Usuario
import sqlalchemy as sa
# from flask_wtf import LoginForm, RegistrationForm
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html', title = 'Log In')

@auth.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', title = 'Cadastro')

@auth.route('/esqueci-senha', methods=['GET', 'POST'])
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