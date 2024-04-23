from flask import render_template, url_for, request
from app import app

@app.route('/')
@app.route('/index', defaults={"nome":"Usuário", "profissao":"Aux. de Aspone", "canal":"Canauxaspone"})
    
@app.route('/index/<nome>/<profissao>/<canal>')
def index(nome, profissao, canal):
    dados = {"profission": profissao, "channel": canal}
    return render_template('index.html', name=nome, data=dados)


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['GET'])
def autenticar():
    usuario = request.args.get('user')
    senha = request.args.get('pwd')

    return "usuario: {} e senha: {}".format(usuario, senha)