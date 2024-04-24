from flask import render_template, request, flash, redirect
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


@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('user')
    senha = request.form.get('pwd')
    if usuario == 'admin' and senha == 'senha123':
        return "usuario: {} e senha: {}".format(usuario, senha)
    else:
        flash("Dados inválidos.")
        return redirect('/login')