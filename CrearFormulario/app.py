from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Correo, Length

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mi_clave_secreta'

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_super_secreta'

# Formulario de registro
class RegistrationForm(FlaskForm):
    name = StringField("Nombre", validators=[
        DataRequired(message="El nombre es obligatorio."),
        Length(min=3, message="El nombre debe tener al menos 3 caracteres.")
    ])
    email = StringField("Correo", validators=[
        DataRequired(message="El correo es obligatorio."),
        Email(message="Debe ser un correo válido.")
    ])
    password = PasswordField("Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria."),
        Length(min=6, message="La contraseña debe tener al menos 6 caracteres.")
    ])
    submit = SubmitField("Registrarse")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Aquí podrías guardar los datos si fuera necesario
        return f"Usuario registrado: {form.name.data} ({form.email.data})"
    return render_template("register.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
