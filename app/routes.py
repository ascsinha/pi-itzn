from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Index')

@app.route('/home')
def home():
    return render_template('main/home.html', title = 'Home')

if __name__ == '__main__':
    app.run(debug = True)