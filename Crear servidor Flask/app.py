from flask import Flask, request, jsonify

app = Flask(__name__)

#Ruta de GET 
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
     "nombre": "Mi primera aplicacion en Flask", 
     "version": "1.0", 
     "autor": "Alanis"
})

#Ruta de POST
@app.route("/mensaje", methods=["POST"])
def mensaje():
    print("Metodo recibido:", request.method)
    if request.method == 'POST':
        data = request.get_json()
        nombre = data.get("nombre", "Usuario")
        return jsonify({
            "respuesta": f"Hola, {nombre}. He recibido tu mensaje: '{mensaje}' "
        })
    else:
        return jsonify({
            "mensaje": "Tiene que utilizar la ruta POST para poder enviar un mensaje"
        })

     
if __name__ == "__main__":
    app.run(debug=True)
    