from flask import Flask, url_for, render_template, request 
import banco

app = Flask(__name__)
condb = banco.condb
banco.create_usuario(condb)

@app.route('/', methods = ['GET', 'POST'])
def tela_login():
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



@app.route('/', methods=['GET', 'POST'])
def fo():
    if request.method == 'POST':
        
        nome = request.form.get('nome')
        email = request.form.get('E-mail')
        senha = request.form.get('senha')
        db = banco.insert_usuario(nome, email, senha)
        render_template('fo.html', db = db)
            
    
if __name__ == '__main__':
    app.run(debug=True)


