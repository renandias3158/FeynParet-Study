from flask import Flask, render_template, request
import banco

app = Flask(__name__)


condb = banco.condb
banco.create_usuario(condb)

@app.route('/canais', methods=['GET'])
def canais():
    return render_template('canais.html')

@app.route('/estudo', methods=['GET'])
def estudo():
    return render_template('estudo.html')

@app.route('/feyn', methods=['GET'])
def feyn():
    return render_template('feyn.html')

@app.route('/fo2', methods=['GET'])
def fo2():
    return render_template('fo2.html')

@app.route('/fontes', methods=['GET'])
def fontes():
    return render_template('fontes.html')

@app.route('/horarios', methods=['GET'])
def horarios():
    return render_template('horarios.html')

@app.route('/mainPage', methods=['GET'])
def mainPage():
    return render_template('mainPage.html')

@app.route('/materiais', methods=['GET'])
def materiais():
    return render_template('materiais.html')

@app.route('/metodos', methods=['GET'])
def metodos():
    return render_template('metodos.html')

@app.route('/metodosestudo', methods=['GET'])
def metodosestudo():
    return render_template('metodosestudo.html')

@app.route('/musicas', methods=['GET'])
def musicas():
    return render_template('musicas.html')

@app.route('/page_login', methods=['GET'])
def page_login():
    return render_template('page_login.html')

@app.route('/page_newaccount', methods=['GET'])
def page_newaccount():
    return render_template('page_newaccount.html')

@app.route('/paret', methods=['GET'])
def paret():
    return render_template('paret.html')

@app.route('/pesquisa', methods=['GET'])
def pesquisa():
    return render_template('pesquisa.html')

@app.route('/pomodoro', methods=['GET'])
def pomodoro():
    return render_template('pomodoro.html')

@app.route('/resumo', methods=['GET'])
def resumo():
    return render_template('resumo.html')

@app.route('/user', methods=['GET'])
def user():
    return render_template('user.html')


@app.route('/login', methods=['GET', 'POST'])
def tela_login():
    erro = ''
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuario = banco.verifica_usuario(email, senha)
        if usuario:
            return f'Login realizado com sucesso, bem-vindo, {email}!'
        else:
            erro = 'Email ou senha incorretos, tente novamente!'
    return render_template('page_login.html', erro=erro)

@app.route('/formulario', methods=['GET', 'POST'])
def fo():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('E-mail')  
        senha = request.form.get('senha')
        banco.insert_usuario(nome, email, senha)
        return render_template('fo.html', db=True)
    return render_template('fo.html', db=False)



if __name__ == '__main__':
    app.run(debug=True)
