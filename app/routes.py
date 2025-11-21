from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Bem-vindo ao ITZN!')

@app.route('/dashboard')
def home():
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

if __name__ == '__main__':
    app.run(debug = True)