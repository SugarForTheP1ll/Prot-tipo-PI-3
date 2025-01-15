from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'PROTPISECRET_KEY'



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vidadigital')
def vida_digital():
    return render_template('vidadigital.html')

@app.route('/videojogos')
def video_jogos():
    return render_template('videojogos.html')

@app.route('/pirata')
def pirataria():
    return render_template('pirataria.html')


@app.route('/comunidades')
def tec():
    return render_template('comunidades.html')


if __name__ == '__main__':
    app.run(debug=True)


