from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import Usuario
from app import db

usuario = Blueprint('usuario', __name__, url_prefix= '/usuario')

@usuario.route('/login-admin', methods = ['POST'])
def usuario_admin():
    usuario_admin = Usuario.query.filter_by(is_admin = True).first()
    
    if not usuario_admin:
        novo_admin = Usuario(senha = 'admin123', tipo_usuario = 'Admin', is_admin = True)
        
        db.session.add(novo_admin)
        db.session.commit()
        flash('Agora você é um administrador!')