from flask import Flask, render_template, request 
import banco

app = Flask(__name__)

banco.create_usuario()

@app.route('/', methods=['GET', 'POST'])
def fo():
    if request.method == 'POST':
        
        nome = request.form.get('nome')
        email = request.form.get('E-mail')
        senha = request.form.get('senha')
        db = banco.insert_usuario(nome, email, senha)
        render_template('fo.html', db = db)
        return "Usuário cadastrado com sucesso!"       
    
if __name__ == '__main__':
    app.run(debug=True)


