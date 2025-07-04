from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    nome = None
    senha = None
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
    return render_template('page_login.html', nome=nome, senha=senha)

@app.route('/newaccount')
def new_account():
    newnome = None
    newsenha = None
    if request.method == 'POST':
        newnome = request.form.get('newnome')
        newsenha = request.form.get('newsenha')
    return render_template('page_newaccount.html', newnome=newnome, newsenha=newsenha)


if __name__ == '__main__':
    app.run(debug=True)


