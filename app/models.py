from flask import current_app
from flask_login import UserMixin
import datetime as dt
import sqlalchemy as sa
from sqlalchemy import and_, or_
import sqlalchemy.orm as so
from typing import Optional
import enum
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
    
class TiposUsuario(enum.Enum):
    __tablename__ = 'tipousuario'
    USUARIO = 'Usuário'
    ADMIN = 'Admin'
    
class Status(enum.Enum):
    __tablename__ = 'status_agendamento'
    EM_ANALISE = 'Em análise'
    ACEITO = 'Agendado'
    NEGADO = 'Negado'

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    id: so.Mapped[int] = so.mapped_column(primary_key = True)
    nome: so.Mapped[str] = so.mapped_column(sa.String(64), nullable = False, unique = True, index = True)
    email: so.Mapped[str] = so.mapped_column(sa.String(128), nullable = False, unique = True, index = True)
    cpf: so.Mapped[str] = so.mapped_column(sa.String(14), unique = True, nullable = False)
    data_nascimento: so.Mapped[dt.date] = so.mapped_column(sa.Date, nullable = False)
    telefone: so.Mapped[str] = so.mapped_column(sa.String(13), unique = True, index = True)
    e_admin: so.Mapped[bool] = so.mapped_column(sa.Boolean, default = False)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256), nullable = False)
    
    agendamentos: so.WriteOnlyMapped['Agendamento'] = so.relationship('Agendamento', back_populates = 'usuario', cascade = 'all, delete-orphan')
    
    def __repr__(self):
        return f'<Usuário {self.nome}>'
    
    def criar_senha(self, senha):
        self.password_hash = generate_password_hash(senha)
        
    def checar_senha(self, senha):
        return check_password_hash(self.password_hash, senha) 
    
    def agendFeito(self, agendamento):
        return agendamento in self.agendamentos
    
class Admin(Usuario):
    id_admin: so.Mapped[int] = so.mapped_column(primary_key = True)
    id_usuario: so.Mapped[int] = so.mapped_column(sa.ForeignKey('usuario.id'))
        
    def agendAceito(self, agendamento):
        if self.agendFeito(agendamento):
            agendamento.validacao == 'Agendado'
            db.session.commit()
        return agendamento.validacao == 'Agendado'
            
    def em_analise(self, agendamento):
        if self.agendFeito(agendamento):
            agendamento.validacao == 'Em análise'
            db.session.commit()
        return agendamento.validacao == 'Em análise'
    
    def negado(self, agendamento):
        if self.agendFeito(agendamento):
            agendamento.validacao == 'Negado'
            db.session.commit()
        return agendamento.validacao == 'Negado'
    
    def __repr__(self):
        return f'<Administrador {self.nome}>'
    
class Agendamento(db.Model):
    __tablename__ = 'agendamento'
    id_agendamento: so.Mapped[int] = so.mapped_column(primary_key = True)
    id_usuario: so.Mapped[int] = so.mapped_column(sa.ForeignKey('usuario.id'), nullable = False)
    data_reserva: so.Mapped[dt.time] = so.mapped_column(sa.Date, nullable = False)
    hora_inicial: so.Mapped[dt.time] = so.mapped_column(sa.Time, nullable = False)
    hora_final: so.Mapped[dt.time] = so.mapped_column(sa.Time, nullable = False)
    validacao: so.Mapped[Status] = so.mapped_column(sa.Enum(Status), nullable = False)
    id_estacao: so.Mapped[int] = so.mapped_column(sa.Integer, nullable = False)
    observacao: so.Mapped[str] = so.mapped_column(sa.String(140), nullable = True)
    
    usuario: so.Mapped['Usuario'] = so.relationship('Usuario', back_populates = 'agendamentos')
            
    def __repr__(self):
        return f'<Agendamento {self.id_agendamento}>'