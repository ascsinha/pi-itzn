from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import Usuario
from app import db

usuario = Blueprint('usuario', __name__, url_prefix= '/usuario')