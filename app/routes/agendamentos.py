from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db

agendamentos = Blueprint('agendamentos', __name__, url_prefix = '/agendamentos')