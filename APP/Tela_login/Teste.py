from flask import Flask, url_for, render_template, request, session, redirect, flash
from flask_session import Session
import os
import banco

app = Flask(__name__)

condb = banco.condb
banco.create_usuario(condb)


@app.route('/canais')
def canais():
   return render_template('canais.html')

@app.route('/estudo')
def estudo():
   return render_template('estudo.html')

@app.route('/feyn')
def feyn():
   return render_template('feyn.html')

@app.route('/fo')
def fo():
   return render_template('fo.html')

@app.route('/fo2')
def fo2():
   return render_template('fo2.html')

@app.route('/fontes')
def fontes():
   return render_template('fontes.html')

@app.route('/horarios')
def horarios():
   return render_template('horarios.html')

@app.route('/mainPage')
def mainPage():
   return render_template('mainPage.html')

@app.route('/materiais')
def materiais():
   return render_template('materiais.html')

@app.route('/metodos')
def metodos():
   return render_template('metodos.html')

@app.route('/metodosestudo')
def metodosestudo():
   return render_template('metodosestudo.html')

@app.route('/musicas')
def musicas():
   return render_template('musicas.html')

@app.route('/', methods = ['GET', 'POST'])
def page_login():
    erro = ''
    if request.method == 'POST':
    
        email = request.form('email')
        senha = request.form('senha')
        usuario =banco.verifica_usuario(email, senha)
        if usuario:
            return f'login realizado com sucesso, bem vindo,{email}!'
        else:
            erro = 'Email ou senha incorretos, tente novamente!'
    return render_template('page_login.html' ,erro=erro)

@app.route('/page_newaccount')
def page_newaccount():
   return render_template('page_newaccount.html')

@app.route('/paret')
def paret():
   return render_template('paret.html')

@app.route('/organizacao')
def organizacao():
   return render_template('organizacao.html')

@app.route('/pesquisa')
def pesquisa():
   return render_template('pesquisa.html')

@app.route('/pomodoro')
def pomodoro():
   return render_template('pomodoro.html')


@app.route('/resumo')
def resumo():
   return render_template('resumo.html')

@app.route('/user')
def user():
   return render_template('user.html')

@app.route('/ambienteestudo')
def ambienteestudo():
   return render_template('ambienteestudo.html')

@app.route('/')
def index():
    return render_template('mainPage.html')

            
    
if __name__ == '__main__':
    app.run(debug=True)
    


