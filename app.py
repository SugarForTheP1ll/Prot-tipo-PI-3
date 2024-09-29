from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        # Aqui você pode adicionar a lógica de autenticação
        if email == "usuario@exemplo.com" and senha == "senha123": 
            return redirect(url_for('sucesso')) 
        else:
            flash('Credenciais inválidas. Tente novamente.')
    
    return render_template('login.html')

# Rota para página após login bem-sucedido
@app.route('/sucesso')
def sucesso():
    return "Login bem-sucedido!"

if __name__ == '__main__':
    app.run(debug=True)
