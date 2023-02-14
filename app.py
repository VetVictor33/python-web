from flask import Flask, render_template

app = Flask(__name__)

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

postsi = [ ]

@app.route('/')
def hello():
    return render_template("exibir_entradas.html", entradas = posts)

@app.route('/pudim')
def pudim():
    return "<h1 style='color:red;'>J'aime le pudim<h1>"
