from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'PROTPISECRET_KEY'



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if email == "usuario@exemplo.com" and senha == "senha123":
            return redirect(url_for('sucesso'))
        else:
            flash('Credenciais inválidas. Tente novamente.')
    
    return render_template('login.html')


@app.route('/home')
def sucesso():
    return render_template('home.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirma_senha = request.form['confirma_senha']

        if senha != confirma_senha:
            flash('As senhas não coincidem!')
            return redirect(url_for('cadastro'))

        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('login'))  

    return render_template('cadastro.html')

@app.route('/comunidades')
def tec():
    return render_template('comunidades.html')

if __name__ == '__main__':
    app.run(debug=True)


