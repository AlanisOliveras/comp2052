from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user,login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "clave_secreta"

login_manager = LoginManager(app)
login_manager .login_view = 'login'

#Modelo de usuario
class User(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id # guarda el id del usuario 
        self.username = username # guarda el nombre del usuario
        self.password = password # guarda el hash de la contraseña
        self.role = role # guarda el rol o permiso del usuario

#Crear datos del usuario  
users = {"Daynna": User(1, "Daynna", generate_password_hash("Nala2014"), "admin"),
         "Javier": User(2, "Javier", generate_password_hash("Vale1546"), "user")}

#Buscar un usuario cuando flask lo necesite
@login_manager.user_loader
def load_user(user_id): #el id del usuario
    for user in users.values(): #recore todos los usuarios
        if str(user.id) == user_id: #Convierte el user en texto str
            return user #Devuelve 
        return None #no encontró el usuario

#Ruta para Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = users.get(username)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for ("dashboard"))
        else:
            return "Nombre de usuario o contraseña incorecta", 401
    return render_template("login.html")

#Ruta para logout
@app.route("/logout")
@login_required 
def logout():
    logout_user()
    return "Sesión cerrada."

#Ruta protegida
@app.route("/dashboard")
@login_required
def dashboard():
    return f"Hola, {current_user.username}! Tu rol es {current_user.role}."

#Pagina principal
@app.route ("/")
def home():
    return render_template("home.html")

if __name__  == "__main__":
    app.run(debug=True)


