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

if __name__ == '__main__':
    app.run(debug=True)


