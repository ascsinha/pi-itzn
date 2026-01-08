from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db

main = Blueprint('main', __name__)

@main.route('/agendamentos')
def agendamentos():
    return render_template('agendamentos.html', title = "Agendamentos")


