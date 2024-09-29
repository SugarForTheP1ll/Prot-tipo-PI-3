from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Rota de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if email == "usuario@exemplo.com" and senha == "senha123":
            return redirect(url_for('sucesso'))  # Redireciona para a página de sucesso
        else:
            flash('Credenciais inválidas. Tente novamente.')
    
    return render_template('login.html')

# Rota de sucesso
@app.route('/sucesso')
def sucesso():
    return render_template('home.html')

# Rota de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirma_senha = request.form['confirma_senha']

        # Verificação simples se as senhas coincidem
        if senha != confirma_senha:
            flash('As senhas não coincidem!')
            return redirect(url_for('cadastro'))

        # Aqui você pode adicionar a lógica para salvar os dados no banco de dados
        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('login'))  # Redireciona para o login após o cadastro

    return render_template('cadastro.html')  # Renderiza a página de cadastro

if __name__ == '__main__':
    app.run(debug=True)
