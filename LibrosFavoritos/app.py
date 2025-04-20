from flask import Flask, render_template

app = Flask(__name__)

libros = [
    {"titulo": "The Maze Runner", "autor": "James Dashner"},
    {"titulo": "Las Crónicas de Narnia", "autor": "C. S. Lewis"},
    {"titulo": "Percy Jackson", "autor": "Rick Riordan"}
]

autores = ["James Dashner", "C. S. Lewis", "Rick Riordan"]

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', titulo="Inicio", mensaje="Bienvenido a mi lista de libros favoritos")

@app.route('/libros', methods=["GET"])
def mostrar_libros():
    return render_template("libros.html", titulo="libros", libros=libros )

@app.route('/autores', methods=["GET"])
def mostrar_autores():
    return render_template("autores.html",titulo="Autores", autores=autores)

if __name__== '__man__':
    app.run(debug=True)
