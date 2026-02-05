from flask import Blueprint, render_template, request, redirect, url_for, flash

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
@index_bp.route('/index')
def index():
    return render_template('index.html', title = 'Bem-vindo ao ITZN!')

@index_bp.route('/editais')
def editais():
    return render_template('main/editais.html', title = 'Editais')

@index_bp.route('/sobre')
def sobre():
    return render_template('main/sobre.html', title = 'Sobre Nós')

@index_bp.route('/contato')
def contato():
    return render_template('main/contato.html', title = 'Contato')