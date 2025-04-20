from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta GET /info
@app.route("/info", methods=["GET"])
def info():
    ({
    "sistema": "Gestor de usuarios ",
    "version": "1.0",
    "descripcion": "API para crear y listar usuarios"
})
   
# Ruta POST /crear_usuario
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = request.get_json()
    nombre= data.get("nombre")
    correo = data.get("correo")

    #validacion de los datos
    if not nombre or not correo:
        return jsonify ({'error': 'Faltan datos: nombre y correo son obligatorios.'})
    
    usuario.append({'nombre': nombre, 'correo': correo})
    return jsonify({'mensaje': 'Usuario creado exitosamente.'})

#Ruta GET para obtener la lista de usuarios
@app.route('/usuario', methods=["GET"])
def obtener_usuario():
    return jsonify(usuario)

if __name__ == "__main__":
    app.run(debug=True)
