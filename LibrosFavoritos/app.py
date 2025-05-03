from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

libros = [
    {"titulo": "The Maze Runner", "autor": "James Dashner"},
    {"titulo": "Las Crónicas de Narnia", "autor": "C. S. Lewis"},
    {"titulo": "Percy Jackson", "autor": "Rick Riordan"}
]

autores = ["James Dashner", "C. S. Lewis", "Rick Riordan"]

recomendaciones = []


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', titulo="Inicio", mensaje="Bienvenido a mi lista de libros favoritos")

@app.route('/libros', methods=["GET"])
def mostrar_libros():
    return render_template("libros.html", titulo="libros", libros=libros )

@app.route('/autores', methods=["GET"])
def mostrar_autores():
    return render_template("autores.html",titulo="Autores", autores=autores)

@app.route('/recomendaciones', methods=['GET', 'POST'])
def recomendaciones_view():
    if request.method == 'POST':
        texto = request.form.get('recomendacion', '').strip()
        if texto:
            recomendaciones.append(texto)
        return redirect(url_for('recomendaciones_view'))

    return render_template("recomendaciones.html", titulo="Recomendaciones", recomendaciones=recomendaciones)


@app.route('/eliminar_recomendacion/<int:index>', methods=['POST'])
def eliminar_recomendacion(index):
    if 0 <= index < len(recomendaciones):
        recomendaciones.pop(index)
        return redirect(url_for('recomendaciones_view'))
    

if __name__== '__main__':
    app.run(debug=True)
