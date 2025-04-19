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
    data = request.get_json()
    nombre = data.get("nombre", "Usuario")
    respuesta = {"respuesta": f"Hola {nombre}, Gracias por tu mensale!"}
    return jsonify(respuesta)
     
if __name__ == "__main__":
    app.run(debug=True)
    