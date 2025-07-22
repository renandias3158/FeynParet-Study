from flask import Flask, url_for, render_template, request, session, redirect, flash
from flask_session import Session
import os
import banco

app = Flask(__name__)
app.secret_key = 'chave_secreta'

condb = banco.condb
banco.create_usuario(condb)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = os.path.join(app.root_path, 'sessions')
app.config['SESSION_PERMANENT'] = False

Session(app)

@app.route('/canais')
def canais():
   return render_template('canais.html')

@app.route('/estudo')
def estudo():
   return render_template('estudo.html')

@app.route('/feyn')
def feyn():
   return render_template('feyn.html')

@app.route('/fo', methods=['GET', 'POST'])
def fo():
    if 'usuario' in session:
        return render_template('fo.html', usuario=session['usuario'])
    metodo = request.form.get('metodoestudo')
    print(f"Método escolhido: {metodo}")
    return redirect(url_for('mainPage'))  

@app.route('/fontes')
def fontes():
   return render_template('fontes.html')

@app.route('/horarios')
def horarios():
   return render_template('horarios.html')

@app.route('/mainPage')
def mainPage():
    if 'usuario' in session:
        return render_template('mainPage.html', usuario=session['usuario'])
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()  
    return redirect(url_for('page_login'))  

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

@app.route('/')
def index():
    if 'usuario' in session:
        return redirect(url_for('mainPage'))
    return render_template('page_login.html')

@app.route('/pagelogin', methods=['GET', 'POST'])
def page_login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuario = banco.verifica_usuario(email, senha)
        
        if usuario:  
            session['usuario'] = usuario[1]  
            return redirect(url_for('mainPage'))
        else:
            flash('Email ou senha incorretos.')
            return redirect(url_for('index'))
    return render_template('page_login.html')




@app.route('/page_newaccount', methods=['GET', 'POST'])
@app.route('/page_newaccount', methods=['GET', 'POST'])
def page_newaccount():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        try:
            usuario = banco.insert_usuario(nome, email, senha)
            flash('Conta criada com sucesso! Você pode fazer login agora.', 'success')
            return redirect(url_for('page_login'))  
        except Exception as e:
            flash('Ocorreu um erro ao criar a conta. Tente novamente.', 'error')
            return redirect(url_for('page_newaccount'))
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
 
if __name__ == '__main__':
    app.run(debug=True)
    


