from flask import render_template, request, redirect, url_for, flash
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Bem-vindo ao ITZN!')

@app.route('/dashboard')
def dashboard():
    return render_template('main/dashboard.html', title = 'Home')

@app.route('/login')
def login():
    return render_template('auth/login.html', title = 'Log In')

@app.route('/cadastro')
def cadastro():
    return render_template('auth/cadastro.html', title = 'Cadastro')

@app.route('/eventos')
def eventos():
    return render_template('main/eventos.html', title = 'Eventos')

@app.route('/editais')
def editais():
    return render_template('main/editais.html', title = 'Editais')

@app.route('/sobre')
def sobre():
    return render_template('main/sobre.html', title = 'Sobre Nós')

@app.route('/contato')
def contato():
    return render_template('main/contato.html', title = 'Contato')

@app.route('/esqueci-senha', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(debug = True)