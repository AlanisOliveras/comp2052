from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config["SECRET_KEY"] = "clave_segura"

class RegistroForm(FlaskForm):
    nombre = StringField("Nombre", validators=[
        DataRequired(message="El nombre es obligatorio."),
        Length(min=3, message="Debe tener al menos 3 caracteres.")
    ])
    correo = StringField("Correo", validators=[
        DataRequired(message="El correo es obligatorio."),
        Email(message="Formato de correo no válido.")
    ])
    password = PasswordField("Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria."),
        Length(min=6, message="Debe tener al menos 6 caracteres.")
    ])
    submit = SubmitField("Registrarse")

@app.route("/", methods=["GET", "POST"])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        return render_template("home.html", mensaje=f"Usuario {nombre} registrado correctamente.")
    return render_template("register.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
