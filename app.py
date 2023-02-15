from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
SECRET_KEY = "pudim"
app.config.from_object(__name__)

# POSTS MOCK
posts = [
    {
        "titulo" : "This is the first title",
        "texto" : "This is the first text"
    },
    {
        "titulo" : "This is the second title",
        "texto" : "And this is the second text"
    },
    {
        "titulo" : "So this is the third title",
        "texto" : "Therefore this is the third text"
    }
]

# USER MOCKS
USARNAME = "admin"
PASSWORD = "admin"

@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas = posts)

@app.route('/login', methods=["GET", "POST"])
def login():
    erro = ""
    if request.method == "POST":
        if request.form['username'] == USARNAME and request.form['password'] == PASSWORD:
            session['logado'] = True
            return redirect(url_for('exibir_entradas'))
        erro = "Usuário ou senha inválidos"
    return render_template("login.html", erro=erro)
