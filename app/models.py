from flask import current_app
from flask_login import UserMixin
import datetime as dt
import sqlalchemy as sa
from sqlalchemy import and_, or_
import sqlalchemy.orm as so
from typing import Optional
import enum
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login

class Generos(enum.Enum):
    __tablename__ = 'generos'
    FEMININO = 'Feminino'
    MASCULINO = 'Masculino'
    TRANSGENERO = 'Transgênero'
    NAOBINARIO = 'Não-binário'
    OUTRO = 'Outro'
    
class TiposUsuario(enum.Enum):
    __tablename__ = 'tipousuario'
    USUARIO = 'Usuário'
    EMPRESA = 'Empresa'
    ADMIN = 'Admin'
    PROFESSOR = 'Professor'

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    id: so.Mapped[int] = so.mapped_column(primary_key = True)
    nome: so.Mapped[str] = so.mapped_column(sa.String(64), nullable = False, unique = True, index = True)
    email: so.Mapped[str] = so.mapped_column(sa.String(128), nullable = False, unique = True, index = True)
    cpf: so.Mapped[str] = so.mapped_column(sa.String(11), unique = True)
    data_nascimento: so.Mapped[dt.date] = so.mapped_column(sa.Date, nullable = False)
    telefone: so.Mapped[str] = so.mapped_column(sa.String(11), unique = True, index = True)
    genero: so.Mapped[Generos] = so.mapped_column(sa.Enum(Generos), nullable = False)
    tipo_usuario: so.Mapped[TiposUsuario] = so.mapped_column(sa.Enum(TiposUsuario), nullable = False, default = TiposUsuario.USUARIO)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    
    def __repr__(self):
        return f'<Usuário {self.nome}>'
    
    def criar_senha(self, senha):
        self.password_hash = generate_password_hash(senha)
        
    def checar_senha(self, senha):
        return check_password_hash(self.password_hash, senha)
    
class Empresa(Usuario):
    id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("usuario.id"), primary_key = True)
    nome_empresa: so.Mapped[str] = so.mapped_column(sa.String(128), nullable = False)
    id_empresa: so.Mapped[int] = so.mapped_column(sa.Integer)
    cnpj: so.Mapped[str] = so.mapped_column(sa.String(14), nullable = False)
    
    def __repr__(self):
        return f'<Empresa {self.nome_empresa}>'
    
class Professor(Usuario):
    id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("usuario.id"), primary_key = True)
    id_professor: so.Mapped[int] = so.mapped_column(sa.Integer)
    matricula: so.Mapped[int] = so.mapped_column(sa.Integer, nullable = False)
    __table_args__ = (
        sa.CheckConstraint(
            or_(
                and_(Usuario.tipo_usuario == TiposUsuario.PROFESSOR, matricula >= 0, matricula <= 999999),
                and_(Usuario.tipo_usuario != TiposUsuario.PROFESSOR, matricula == None)
            ),
            name = "ck_matricula_range"
        ),
    )
    
    def __repr__(self):
        return f'<Professor {self.nome}>'
    
class Admin(Usuario):
    id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("usuario.id"), primary_key = True)
    id_admin: so.Mapped[int] = so.mapped_column(sa.Integer)
    
    def __repr__(self):
        return f'<Administrador {self.nome}>'