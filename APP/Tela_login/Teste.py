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
    if request.method == 'POST':
        metodo_escolhido = request.form.get('metodoestudo')
        if metodo_escolhido:
            metodo_lower = metodo_escolhido.lower()
            if metodo_lower == 'resumos':
                return render_template("resumo.html")
            metodo_banco = metodo_escolhido.capitalize()
            resultado = banco.verifica_metodo(metodo_banco)
            if not resultado:
                banco.insert_metodo(condb, metodo_banco)
                resultado = banco.verifica_metodo(metodo_banco)
            id_metodo = resultado[0]

            if metodo_lower == 'pomodoro':
                return redirect(url_for('pagina_pomodoro', id_metodo=id_metodo))
            elif metodo_lower == 'feynman':
                return redirect(url_for('pagina_feynman', id_metodo=id_metodo))
            elif metodo_lower == 'pareto':
                return redirect(url_for('pagina_paret', id_metodo=id_metodo))
            else:
                return "<h2>Método reconhecido, mas sem ação definida.</h2>"
        else:
            return "<h2>Nenhum método escolhido.</h2><a href='/fo'>Voltar</a>"
    else:
        return render_template("fo.html")
    
@app.route('/pomodoro/<int:id_metodo>')
def pagina_pomodoro(id_metodo):
    dados = banco.verifica_pomodoro(id_metodo)
    return render_template('pomodoro.html', dados=dados)

@app.route('/feynman/<int:id_metodo>')
def pagina_feynman(id_metodo):
    dados = banco.verifica_feynman(id_metodo)
    return render_template('feyn.html', dados=dados)

@app.route('/paret/<int:id_metodo>')
def pagina_paret(id_metodo):
    dados = banco.verifica_pareto(id_metodo)
    return render_template('paret.html', dados=dados)

@app.route('/resumos/<int:id_metodo>')
def pagina_resumo(id_metodo):
    
    return render_template("resumo.html", id_metodo=id_metodo)

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

@app.route('/user', methods=['GET', 'POST'])
def user():
    if 'usuario' not in session:
        return redirect(url_for('page_login'))

    usuario_nome = session['usuario']
    usuario = banco.get_usuario_por_nome(condb, usuario_nome)

    if not usuario:
        flash('Usuário não encontrado.', 'error')
        return redirect(url_for('page_login'))

    id_usuario, nome, email, senha = usuario

    if request.method == 'POST':
        novo_nome = request.form.get('nome')
        novo_email = request.form.get('email')
        nova_senha = request.form.get('senha')

        try:
            banco.update_usuario(condb, id_usuario, novo_nome, novo_email, nova_senha)
            session['usuario'] = novo_nome  
            flash('Dados atualizados com sucesso!', 'success')
            return redirect(url_for('user'))
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            flash('Erro ao atualizar os dados.', 'error')

    return render_template('user.html', usuario={'nome': nome, 'email': email, 'senha': senha})

@app.route('/deletar_usuario', methods=['POST'])
def deletar_usuario():
    if 'usuario' not in session:
        return redirect(url_for('page_login'))

    usuario_nome = session['usuario']
    usuario = banco.get_usuario_por_nome(condb, usuario_nome)

    if not usuario:
        flash('Usuário não encontrado.', 'error')
        return redirect(url_for('page_login'))

    id_usuario = usuario[0]

    try:
        banco.delete_usuario(condb, id_usuario)
        session.pop('usuario', None)  # Remove usuário da sessão
        flash('Conta deletada com sucesso.', 'success')
        return redirect(url_for('page_login'))
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")
        flash('Erro ao deletar conta.', 'error')
        return redirect(url_for('user'))

@app.route('/ambienteestudo')
def ambienteestudo():
   return render_template('ambienteestudo.html')
 
if __name__ == '__main__':
    app.run(debug=True)