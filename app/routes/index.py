from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db

index = Blueprint('index', __name__)

@index.route('/')
@index.route('/index')
def index():
    return render_template('index.html', title = 'Bem-vindo ao ITZN!')

@index.route('/eventos')
def eventos():
    return render_template('eventos.html', title = 'Eventos')

@index.route('/editais')
def editais():
    return render_template('editais.html', title = 'Editais')

@index.route('/sobre')
def sobre():
    return render_template('sobre.html', title = 'Sobre Nós')

@index.route('/contato')
def contato():
    return render_template('contato.html', title = 'Contato')