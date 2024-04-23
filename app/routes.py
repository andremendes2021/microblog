from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    nome = "Nabu"
    dados = {"profissão": "Aspone", "canal": "Aspone Nabu"}
    return render_template('index.html', name=nome, data=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')