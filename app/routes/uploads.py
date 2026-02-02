from flask import Blueprint, render_template, request, redirect, url_for, flash

uploads = Blueprint('uploads', __name__, url_prefix = '/uploads')
